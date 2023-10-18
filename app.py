import streamlit as st
import lang
import wiki
import aloud

st.set_page_config(page_title="Vetri's Website", page_icon=':books:',layout="wide")

st.latex("SMART")
input_text= st.text_input(label="Ask a question")

if input_text:
    
    as_palm = lang.palm_output(input_text)
    as_wiki=wiki.wiki_output(input_text)

    st.markdown("As per the chatgpt info")
    gpt_text=st.write(as_palm)

    button_gpt_audio=st.button(label="Read")

    if button_gpt_audio:
        audio=aloud.text_to_speech_gpt(as_palm)



    st.markdown("As per the wikipedia info")
    wiki_text=st.write(as_wiki)

     button_wiki_audio=st.button("Read")

    if button_wiki_audio:
        audio=aloud.text_to_speech_wiki(as_wiki)