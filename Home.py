import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_icon=":taxi:")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Thomas Ellyatt")
    content = """
    Hi, I'm Tom, I do stuff with data.
    """
    st.info(content)

col3, empty_col, col4 = st.columns([1, 0.5, 1])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        if row["title"] == 'Portfolio Website':
            st.write(f"[Source Code]({row['url']})")
        else:
            st.write(f"[View App]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        if row["title"] == 'Portfolio Website':
            st.write(f"[Source Code]({row['url']})")
        else:
            st.write(f"[View App]({row['url']})")
