
import streamlit as st
import streamlit.components.v1 as components
import base64


st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":sunflower:",

    )

st.write("# Keyword search")



HtmlFile = open("german_keywords.html", 'r', encoding='utf-8')

raw_html = HtmlFile.read().encode("utf-8")
raw_html = base64.b64encode(raw_html).decode()
components.iframe(f"data:text/html;base64,{raw_html}", height=800)

progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()
