import streamlit as st
import os
import openai

# Load environment variables from .env if available
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Discreet Writing", layout="centered")
st.title("Discreet Writing: Brian Eno–Style Text Generator")

# User inputs
line1 = st.text_input("Line #1", placeholder="Enter first seed line...")
line2 = st.text_input("Line #2", placeholder="Enter second seed line...")

echo   = st.slider("Echo",   min_value=0.0, max_value=1.0, value=0.5)
delay  = st.slider("Delay",  min_value=0.0, max_value=1.0, value=0.5)
timbre = st.slider("Timbre", min_value=0.0, max_value=1.0, value=0.5)

if st.button("Generate Expansion"):
    if not line1 or not line2:
        st.error("Please enter both seed lines.")
    else:
        # Build prompt based on slider values
        def build_prompt(a, b, e, d, t):
            echo_n    = max(1, int(e * 5))
            delay_n   = max(1, int((1-d) * 6))
            timbre_t  = "lush and reverberant" if t > 0.5 else "sparse and dry"
            return (
                f"You are an echo chamber.\n"
                f"Given two lines:\n 1) '{a}'\n 2) '{b}'\n"
                f"• Repeat key phrases {echo_n} times with subtle variation.\n"
                f"• Introduce new themes after every {delay_n} sentences.\n"
                f"• Use a {timbre_t} tone and poetic imagery.\n"
                f"Generate a single paragraph weaving and layering these lines in the style of Brian Eno’s Discreet Music."
            )
        prompt = build_prompt(line1, line2, echo, delay, timbre)

        # Call OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message["content"]
        st.markdown("### Generated Text")
        st.write(result)
