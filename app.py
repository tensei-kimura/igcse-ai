import streamlit as st
import requests

st.title("IGCSE Science AI Question Generator")

# ユーザーが選ぶ項目
subject = st.selectbox("Choose a subject", ["Physics", "Chemistry", "Biology"])
topic = st.selectbox("Choose a topic", ["Forces", "Waves", "Atoms", "Photosynthesis"])
question_type = st.selectbox("Question type", ["Multiple Choice", "Short Answer"])

# Hugging Face APIの情報
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
API_KEY = st.secrets["huggingface"]["api_key"]  # secrets.toml または Streamlit Cloud Secrets から読み込む

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# AIへの問い合わせ関数
def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# ボタンを押したときの処理
if st.button("Generate Question"):
    prompt = f"Create a high-quality {question_type} question for IGCSE {subject} on the topic '{topic}'. Include 4 options, answer, and explanation."
    st.write("### Result")

    output = query({"inputs": prompt})

    # 出力チェックと表示
    if isinstance(output, list) and "generated_text" in output[0]:
        st.success("✅ AI has generated the question successfully!")
        st.write(output[0]["generated_text"])
    else:
        st.error("❌ AI did not return the expected result. Please try again.")
        st.write("Here is the raw output from the model (for debugging):")
        st.json(output)

