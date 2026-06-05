import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Real-Time AI Internship Finder")

# -------- USER INPUT --------

interest = st.selectbox(
"Career Interest",
["data science","machine learning","marketing","biotech"]
)

location = st.selectbox(
"Preferred Location",
["remote","delhi","bangalore","hyderabad"]
)

# -------- SCRAPER --------

def fetch_internships(keyword):

    url = f"https://internshala.com/internships/{keyword}-internship"

    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")

    jobs = soup.find_all("div",class_="individual_internship")

    results = []

    for job in jobs:

        try:
            role = job.find("h3").text.strip()
            company = job.find("h4").text.strip()

            results.append({
                "Role":role,
                "Company":company
            })

        except:
            pass

    return pd.DataFrame(results)

# -------- BUTTON --------

if st.button("Find Live Internships"):

    st.write("Fetching live internships...")

    df = fetch_internships(interest)

    if len(df) == 0:
        st.write("No internships found")
    else:
        st.write("Top Opportunities")
        st.dataframe(df)