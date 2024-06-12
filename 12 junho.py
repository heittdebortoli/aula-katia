import streamlit as st
import speech_recognition as sr

st.tittle("transcrição")
upload=st.file_uploader("faça upload",type=["wav"])
if upload is not None:
    recognizer=sr.Recognizer()
    with sr.AudioFile(file) as source:
        st.write("processando audio")
        audio=recognizer.record(source)
        texto=recognizer.reconize_google(audio,language="pt-BR")
        st.write("texto: ",texto)
