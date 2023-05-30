import streamlit as st
import torch
import soundfile as sf
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

def generate_audio(text):
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs)
    speech = outputs[0].numpy()
    return speech

def main():
    st.title("Text-to-Speech Demo")
    text = st.text_input("Enter text")

    if st.button("Generate Audio"):
        wav = generate_audio(text)
        sf.write("speech.wav", wav, samplerate=22050)
        st.success("Audio generated successfully. You can download it below.")
        st.audio("speech.wav")

if __name__ == "__main__":
    main()
