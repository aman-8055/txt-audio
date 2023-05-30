import streamlit as st
from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
import IPython.display as ipd

def generate_audio(text):
    models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
        "facebook/fastspeech2-en-ljspeech",
        arg_overrides={"vocoder": "hifigan", "fp16": False}
    )
    model = models[0]
    TTSHubInterface.update_cfg_with_data_cfg(cfg, task.data_cfg)
    generator = task.build_generator(model, cfg)

    sample = TTSHubInterface.get_model_input(task, text)
    wav, rate = TTSHubInterface.get_prediction(task, model, generator, sample)
    
    return wav, rate

def main():
    st.title("Text-to-Speech Demo")
    text = st.text_input("Enter text")

    if st.button("Generate Audio"):
        wav, rate = generate_audio(text)
        st.audio(wav, format="audio/wav", start_time=0)

if __name__ == "__main__":
    main()
