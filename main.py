import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Privacy Policy Analyzer",
    page_icon="🎈",
)


# def _max_width_():
#     max_width_str = f"max-width: 1400px;"
#     st.markdown(
#         f"""
#     <style>
#     .reportview-container .main .block-container{{
#         {max_width_str}
#     }}
#     </style>
#     """,
#         unsafe_allow_html=True,
#     )


# _max_width_()


st.title('Privacy Policy Analyzer')

with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   The *Privacy Policy Analyzer* app is an easy-to-use interface built in Streamlit to help users understand high level risks of a privacy policy
-   It uses a custom parser that leverages NLP and other language packages
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste Privacy Policy URL **")

privacy_policy_url = st.text_input("Here:")

st.write('The url input is: ', privacy_policy_url)

col1, col2, col3 = st.columns(3)
col1.metric("Reading complexity", "70 °F", "1.2 °F")
col2.metric("Total Length", "9", "-8% to average")
col3.metric("Place Holder metric", "22", "4%")


st.text("🚩 - Risk #1")
st.text("🚩 - Risk #2")
st.text("🚩 - Risk #3")
