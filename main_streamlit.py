import random
import streamlit as st
import pandas as pd
import nltk
# from web_scraper import scrape_privacy_policy_url
# from policy_scores import readability_score, word_count

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

from readability import Readability

nltk.download('punkt')


def readability_score(text):
    """

    :param text: privacy policy raw text
    :returns: Flesch–Kincaid readability score

    """
    r = Readability(text)

    return round(r.flesch_kincaid().score)


def word_count(text):
    """

    :param text: privacy policy raw text
    :returns: total number of words in text

    """
    return (len(text.strip().split(" ")))


def scrape_privacy_policy_url(url):
    """

    :param url: url of text
    :returns: privacy policy text

    """

    if url == '':
        return "No url input"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")

    web_text = page_soup.find_all("p")
    output = ' '.join([item.text for item in web_text])

    return output


st.set_page_config(
    page_title="Privacy Policy Analyzer",
    page_icon="🎈",
)

st.image("img/privacy-dash-logo.png")

# title and introductory text
st.title('Privacy Policy Analyzer')

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   The *Privacy Policy Analyzer* app is an easy-to-use interface built in Streamlit to help users understand high level risks of a privacy policy
-   It uses a custom parser that leverages NLP and other language packages
	    """
    )

    st.markdown("")

# user inputs
st.markdown("## **📌 Paste Privacy Policy URL **")

privacy_policy_url = st.text_input("Here:")

# get text from url
privacy_policy_str = scrape_privacy_policy_url(privacy_policy_url)

st.write('The url input is: ', privacy_policy_url)

# initial values before user inputs url
if privacy_policy_url == '':
    reading_score = 'NA'
    word_total = 'NA'
    time_to_read = 'NA'

else:
    st.balloons()
    reading_score = readability_score(privacy_policy_str)
    word_total = word_count(privacy_policy_str)
    time_to_read = round(word_total/250)

# metrics display
col1, col2, col3 = st.columns(3)
col1.metric("Reading Grade Level", reading_score)
col2.metric("Total Length", str(word_total) + ' words')
col3.metric("Estimated Time to Read", str(time_to_read) + ' minutes')


# flags display

st.markdown("## Policy Flags")
flag_list = ['Data Retention', 'Data Security', 'Do Not Track',
             'First Party Collection/Use', 'International and Specific Audiences',
             'Introductory/Generic', 'Other', 'Policy Change', 'Practice not covered',
             'Privacy contact information', 'Third Party Sharing/Collection',
             'User Access, Edit and Deletion', 'User Choice/Control']
for count, flag in enumerate(flag_list):
    if random.random() >= 0.5:
        st.text("🚩 - " + flag)
