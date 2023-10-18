from gtts import gTTS
import app

def text_to_speech_gpt(gpt_text):
    languge="en"
    tex=gpt_text

    speech_output=gTTS(text=tex,lang=languge,slow=False)
    audio=speech_output.save("gpt_output.mp3")
    return audio

def text_to_speech_wiki(wiki_text):
    languge="en"
    tex=wiki_text

    speech_output=gTTS(text=tex,lang=languge,slow=False)
    audio=speech_output.save("wiki_output.mp3")
    return audio