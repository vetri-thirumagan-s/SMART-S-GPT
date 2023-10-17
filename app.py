import streamlit as st
import lang
import wiki

st.set_page_config(page_title="Vetri's Website", page_icon=':books:',layout="wide")

st.latex("SMART")
input_text= st.text_input(label="Ask a question")

if input_text:
    as_palm = lang.palm_output(input_text)
    as_wiki=wiki.wiki_output(input_text)

    st.markdown("As per the chatgpt info")
    st.write(as_palm)

    st.markdown("As per the wikipedia info")
    st.write(as_wiki)