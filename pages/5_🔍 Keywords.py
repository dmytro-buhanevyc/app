
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":sunflower:",

    )

st.write("# Keyword search")



HtmlFile = open("https://github.com/dmytro-buhanevyc/app/blob/main/various/german_keywords.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code)

progress_bar = st.sidebar.progress(0)
# We clear elements by calling empty on them.
progress_bar.empty()
