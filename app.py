import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pydub import AudioSegment

def generate_audio(text):
    # Load T5 model and tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    model = T5ForConditionalGeneration.from_pretrained("t5-base")

    # Encode the input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate speech from text
    with torch.no_grad():
        outputs = model.generate(input_ids)
    
    return outputs

def main():
    st.title("Text-to-Speech Demo")
    text = st.text_input("Enter text")

    if st.button("Generate Audio"):
        outputs = generate_audio(text)

        # Convert the generated IDs to audio
        audio = AudioSegment.from_wav(outputs.tostring())

        # Save the audio to a file
        audio.export("output.wav", format="wav")

        # Play the audio in the Streamlit app
        st.audio("output.wav")

if __name__ == "__main__":
    main()
