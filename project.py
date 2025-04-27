import streamlit as st # type: ignore
from groq import Groq # type: ignore

# Set up Groq client with secret key from Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="Story Helper for Kids", layout="centered")
st.title("Story Helper for Kids 🚀📚")

# Allow user to input any topic
user_topic = st.text_input("Enter any story topic you want:")

user_prompt = ""
if user_topic:
    user_prompt = (
        f"Write a short, engaging story for childr  en about {user_topic}. "
        "The story should be educational and under 200 words. End with a summary of the lesson."
    )

if st.button("Generate Story") and user_prompt:
    with st.spinner("Creating your story..."):
        # Call Groq API (choose a supported model, e.g., 'llama3-8b-8192' or 'llama3-70b-8192')
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_prompt}]
        )
        story = response.choices[0].message.content
        st.markdown("### Your Story")
        st.write(story)
