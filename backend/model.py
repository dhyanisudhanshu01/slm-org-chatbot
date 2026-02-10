import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

model_name = "microsoft/phi-2"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32, device_map="cpu")
    model.eval()
    return tokenizer, model

def generate_response(prompt, max_token=150):
    tokenizer, model = load_model()

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_token,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)