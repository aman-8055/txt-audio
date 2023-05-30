import streamlit as st
from transformers import Tacotron2ForTextToSpeech, Tacotron2Processor
import torch
import soundfile as sf

@st.cache(allow_output_mutation=True)
def load_model():
    processor = Tacotron2Processor.from_pretrained("tugstugi/tacotron2")
    model = Tacotron2ForTextToSpeech.from_pretrained("tugstugi/tacotron2")
    return processor, model

def generate_speech(text, processor, model):
    inputs = processor(text, return_tensors="pt")
    with torch.no_grad():
        model.eval()
        speech = model.generate(inputs.input_ids)
    return speech[0].numpy()

def main():
    st.title("Text-to-Speech Demo")
    text = st.text_input("Enter text")

    # Load the model
    processor, model = load_model()

    if st.button("Generate Audio"):
        speech = generate_speech(text, processor, model)
        sf.write("speech.wav", speech, samplerate=22050)
        st.audio("speech.wav", format="audio/wav")

if __name__ == "__main__":
    main()
