import os
import streamlit as st
from openai import OpenAI

# Set your OpenAI API key (uses Streamlit secrets or environment variable)
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("🛡️ AI Security Assistant Chatbot")
st.write("Enter your security logs, incidents, or CVE descriptions below:")

# User input
user_input = st.text_area("Paste Logs / CVE / Incidents")

# Analyze button
if st.button("Analyze"):
    if not api_key:
        st.error("API key not set. Please add your OpenAI API key in Streamlit Secrets.")
    elif not user_input.strip():
        st.warning("Please enter some logs, CVEs, or incidents to analyze.")
    else:
        # Call the OpenAI Chat API (new style)
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a cybersecurity expert AI assistant. Analyze the provided logs, CVE, or incidents and provide actionable insights, potential risks, and recommended mitigations."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=1000,
                temperature=0.2
            )
            # Display response
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error calling OpenAI API: {e}")
