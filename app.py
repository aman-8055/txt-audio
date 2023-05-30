import streamlit as st
import torch
import soundfile as sf
from transformers import AutoTokenizer, AutoModelForTextToSpeech

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("tts_models/ljspeech")
model = AutoModelForTextToSpeech.from_pretrained("tts_models/ljspeech")

def generate_audio(text):
    # Encode input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate audio
    with torch.no_grad():
        output = model.generate(input_ids)

    # Save audio to file
    audio = output[0].numpy()
    sf.write("output.wav", audio, samplerate=22050)

def main():
    st.title("Text-to-Speech Demo")
    text = st.text_input("Enter text")

    if st.button("Generate Audio"):
        generate_audio(text)
        st.audio("output.wav")

if __name__ == "__main__":
    main()
