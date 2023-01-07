import streamlit as st
from send_email import send_email


with st.form(key="contact_us"):
    user_email = st.text_input("Your email address")
    content = st.text_area("Enter your feedback below")

    button = st.form_submit_button("Send it!")

    if button:
        send_email(user_email, content)
        st.info("Email Sent!")
