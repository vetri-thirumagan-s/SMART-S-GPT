import streamlit as st
import lang
import wiki
import aloud
import image_to_text
# from PIL import Image
# import pytesseract as tess
# import cv2
# tess.pytesseract.tesseract_cmd=r'C:\Users\vetri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="Vetri's Website", page_icon=':books:',layout="wide")

st.latex("SMART")

smart_lens=st.button("SMART LENS")

if smart_lens:

    text=image_to_text.capture()
    cam_text=st.write(text)

    input_text= st.text_input(label="Ask a question",value=text)

else:
    input_text= st.text_input(label="Ask a question")

if input_text:
    
    as_palm = lang.palm_output(input_text)
    as_wiki=wiki.wiki_output(input_text)

    st.markdown("As per the chatgpt info")
    gpt_text=st.write(as_palm)

    button_gpt_audio=st.button(label="Read GPT")

    if button_gpt_audio:
        audio=aloud.text_to_speech_gpt(as_palm)
        audio_output_gpt=open('gpt_output.mp3','rb')
        st.audio(audio_output_gpt)


    st.markdown("As per the wikipedia info")
    wiki_text=st.write(as_wiki)

    button_wiki_audio=st.button("Read WIKI")

    if button_wiki_audio:
        audio=aloud.text_to_speech_wiki(as_wiki)
        audio_output_wiki=open('wiki_output.mp3','rb')
        st.audio(audio_output_wiki)

