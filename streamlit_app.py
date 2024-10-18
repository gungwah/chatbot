import streamlit as st
from transformers import pipeline, set_seed

# Show title and description.
st.title("Deploying GPT2")
st.write(
    "This is a simple app that uses OpenAI's GPT-2 model to generate responses. "
    ""
)
st.markdown("made by **Agung Ngurah Oka Abhina** BUID 15387312. :medal: :medal: :tada:")


# Textbox for user prompt
prompt = st.text_input("Enter your prompt:")

# Textbox for number of tokens
num_tokens = st.number_input("Number of tokens:", min_value=10, max_value=250, value=20)

# Initialize the GPT-2 pipeline
generator = pipeline('text-generation', model='gpt2')

# Function to generate text
def generate_text(prompt, num_tokens, creativity):
    set_seed(42)  # For reproducibility, optional
    if creativity == "High":
        # Higher temperature for more creative output
        return generator(prompt, max_length=num_tokens, temperature=1.0, do_sample=True)[0]['generated_text']
    else:
        # Lower temperature for more predictable output
        return generator(prompt, max_length=num_tokens, temperature=0.7, do_sample=True)[0]['generated_text']

# Button to generate text
if st.button("Generate Text"):
    # Generate responses with different creativity levels
    creative_response = generate_text(prompt, num_tokens, "High")
    predictable_response = generate_text(prompt, num_tokens, "Low")

    # Display the responses
    st.header("Creative Response:")
    st.write(creative_response)

    st.header("Predictable Response:")
    st.write(predictable_response)
