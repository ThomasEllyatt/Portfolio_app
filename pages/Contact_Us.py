import streamlit as st
import pandas as pd
import re
from send_email import send_email
from time import sleep

df = pd.read_csv("topics.csv")

with st.form(key="contact_us"):
    user_email = st.text_input("Your email address")
    topic_selected = st.selectbox('What topic would you like to discuss?', df["topic"])
    message = st.text_area("Enter your feedback below")
    button = st.form_submit_button("Send it!")

    if button:
        if re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', user_email):
            with st.spinner(text='In progress'):
                send_email(user_email, topic_selected, message)
                sleep(1)
                st.success('Email Sent!')
        else:
            st.warning("Please enter a valid email address")
