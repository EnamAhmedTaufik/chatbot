import streamlit as st
import requests
import os

st.header('GPT for Question-Answer', divider='rainbow')
st.image("https://techstartups.com/wp-content/uploads/2024/04/gpt2-chatbot-launched.jpg")

st.markdown(
    """
    <div style="text-align: center;">
        GPT2-chatbot
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; background-color: #f63366; padding: 10px;">
            New chat
        </div>
        """,
        unsafe_allow_html=True
    )

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

model_id = "gpt2"  # or another model from Hugging Face
url = f"https://api-inference.huggingface.co/models/{model_id}"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

def ask_question(question):
    data = {"inputs": question}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_content = response.json()
        # print("Response JSON:", response_content)  # Debug print
        return response_content
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

st.title("Try GPT2 model for QnA")
question = st.text_input("Ask:")

if st.button("Answer Me"):
    result = ask_question(question)[0]['generated_text'].split('?')
    st.write(f'<div style="text-align: center; background-color:#f63366; padding:20px; border-radius:5px;">{result[1]}</div>', unsafe_allow_html=True)