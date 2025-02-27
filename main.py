import streamlit as st
import requests

# Set the page configuration
st.set_page_config(
    page_title="Titanic Dataset Chatbot",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS to improve appearance
st.markdown(
    """
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .stButton > button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #0056b3;
            color: white;
        }
        .stTextInput > div > input {
            border: 1px solid #007bff;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Title
st.title("🚢 Titanic Dataset Chatbot")

# Subtitle
st.markdown("Ask me any question about the Titanic dataset!")

# Input for user question
user_question = st.text_input("💬 Enter your question:")

# Submit button with some spacing
st.markdown("<br>", unsafe_allow_html=True)
if st.button("💡 Get Answer"):
    if user_question:
        with st.spinner("Thinking..."):
            try:
                # Send the question to the FastAPI backend
                response = requests.post(
                    "http://localhost:8501/query/", json={"question": user_question}
                )

                if response.status_code == 200:
                    data = response.json()

                    # Display the answer
                    if "answer" in data:
                        st.success("✅ Answer:")
                        st.write(data["answer"])

                    # Display the image if it exists
                    if "image" in data:
                        st.image(data["image"], caption="Generated Plot", use_column_width=True)
                else:
                    st.error(f"❌ Error: Unable to process your request (Status Code: {response.status_code})")
                    st.write(response.text)
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a question.")

# Sidebar for instructions
with st.sidebar:
    st.header("📖 Instructions")
    st.write(
        """
        - Ask questions like:
          - *What percentage of passengers were male?*
          - *Show the histogram of passenger ages.*
          - *What was the average ticket fare?*
          - *How many passengers embarked from each port?*
        - Click **Submit** to get the answer.
        """
    )
    st.write("---")
    st.info("Developed with ❤️ by Mrunal R K")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <hr>
    <footer style='text-align: center; font-size: small;'>
        © 2025 Titanic Dataset Chatbot. All rights reserved.
    </footer>
    """,
    unsafe_allow_html=True,
)
