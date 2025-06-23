import streamlit as st
from transformers import pipeline

# Load a lightweight text generation model
generator = pipeline("text-generation", model="google/flan-t5-small")

st.title("IGCSE Science AI Question Generator")

# Dropdown for subject selection
subject = st.selectbox("Select a subject:", ["Physics", "Chemistry", "Biology"])

# Dropdown for topic selection
topic = st.selectbox("Select a topic:", ["Forces", "Waves", "Atoms", "Digestion", "Photosynthesis"])

# Dropdown for question type
question_type = st.selectbox("Choose the type of question:", ["Multiple Choice", "Short Answer"])

# Button to generate question
if st.button("Generate Question!"):
    prompt = f"Create a simple {question_type} question for IGCSE {subject} on the topic {topic}. Include the answer and explanation."
    result = generator(prompt, max_length=150)[0]["generated_text"]

    # Display result
    st.write("### Question, Answer & Explanation")
    st.write(result)
