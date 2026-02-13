import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

from backend.rag import BitextRAG

rag = BitextRAG()

model_name = "microsoft/phi-2"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32, device_map="cpu")
    model.eval()
    return tokenizer, model

def generate_response(user_question, max_tokens=150):
    tokenizer, model = load_model()

    retrieved_context = rag.retrieve(user_question)

    context = "\n".join(retrieved_context)

    prompt = f"""
You are a professional customer support chatbot.
Use the context below to answer the question.

Context:
{context}

Question:
{user_question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.6,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded.split("Answer:")[1].strip()
