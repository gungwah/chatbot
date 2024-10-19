import streamlit as st
from transformers import pipeline

st.title("Deploying GPT2")
st.write(
    "This is a simple app that uses OpenAI's GPT-2 model to generate responses. "
    ""
)
st.markdown("made by **Agung Ngurah Oka Abhina** BUID 15387312. :medal: :medal: :tada:")


prompt = st.text_input("Enter your prompt:")

num_tokens =  st.slider("Number of tokens", 10, 100, 25)

generator = pipeline('text-generation', model='gpt2')

# Function to generate text
def generate_text(prompt, num_tokens, creativity):
    if creativity == "High":
        # Higher temperature  and do_sample = true for more creative output
        return generator(prompt, max_length=num_tokens, temperature=1.0, do_sample=True)[0]['generated_text']
    else:
        # Lower temperature do_sample = false for more predictable output
        return generator(prompt, max_length=num_tokens, temperature=0.6, do_sample=False)[0]['generated_text']
    
    #The creative one will produce something different for each run, while the less creative one will produce something similar for each run.


if st.button("Generate Text"):
   
    creative_response = generate_text(prompt, num_tokens, "High")
    predictable_response = generate_text(prompt, num_tokens, "Low")

    st.subheader("Creative Response:", divider="gray")
    st.write(creative_response)

    st.subheader("Predictable Response:", divider="gray")
    st.write(predictable_response)
