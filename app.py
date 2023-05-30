import streamlit as st
import torch
from transformers import Tacotron2ForTextToSpeech, Tacotron2Processor
from pydub import AudioSegment

def generate_audio(text):
    # Load Tacotron2 model and processor
    processor = Tacotron2Processor.from_pretrained("tugstugi/tacotron2")
    model = Tacotron2ForTextToSpeech.from_pretrained("tugstugi/tacotron2")

    # Generate speech from text
    inputs = processor(text, return_tensors="pt", padding=True)
    with torch.no_grad():
        wav = model.generate(inputs["input_ids"], inputs["attention_mask"])
    
    return wav

def main():
    st.title("Text-to-Speech Demo")
    text = st.text_input("Enter text")

    if st.button("Generate Audio"):
        wav = generate_audio(text)
        audio = AudioSegment.from_wav(wav.tostring())

        # Save the audio to a file
        audio.export("output.wav", format="wav")

        # Play the audio in the Streamlit app
        st.audio("output.wav")

if __name__ == "__main__":
    main()
