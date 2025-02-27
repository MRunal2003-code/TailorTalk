import streamlit as st
import requests
import subprocess
import os
import time

# Start FastAPI backend
backend_process = subprocess.Popen([
    "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501", "--reload"
])

# Streamlit frontend
st.set_page_config(page_title="Titanic Dataset Chatbot", layout="wide")
st.title("🚢 Titanic Dataset Chatbot")

st.sidebar.header("📖 Instructions")
st.sidebar.write(
    """
    - Ask questions like:
        - What percentage of passengers were male?
        - Show the histogram of passenger ages.
        - What was the average ticket fare?
        - How many passengers embarked from each port?
    - Click Submit to get the answer.
    """
)

st.sidebar.markdown("---")
st.sidebar.write("Developed with ❤️ by Mrunal R K")

st.write("Ask me any question about the Titanic dataset!")
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    try:
        response = requests.post("http://localhost:8501/query", json={"question": question})
        if response.status_code == 200:
            st.success(response.json().get("answer", "No answer found"))
        else:
            st.error(f"Error: Unable to process your request (Status Code: {response.status_code})")
    except requests.exceptions.ConnectionError:
        st.error("Backend service is not available.")

if st.button("Stop Backend"):
    backend_process.terminate()
