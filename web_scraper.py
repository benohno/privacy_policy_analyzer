from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


def scrape_privacy_policy_url(url):

    if url == '':
        return "No url input"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")

    web_text = page_soup.find_all("p")
    output = ' '.join([item.text for item in web_text])

    return output
