from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get responses from Gemini Pro model
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([question])
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Define the tweet classification function using Gemini
def classify_tweet(tweet_text):
    prompt = "Classify the following tweet as 'Non Spam' or 'Spam':\n\n"
    classification_examples = [
        {"label": "Non Spam", "text": "This is a relevant tweet."},
        {"label": "Spam", "text": "Buy now! Special offer!"}
    ]
    for example in classification_examples:
        prompt += f"Tweet: \"{example['text']}\"\nClassification: {example['label']}\n"
    prompt += f"Tweet: \"{tweet_text}\"\nClassification:"

    return get_gemini_response(prompt)

# Streamlit app layout
def main():
    st.set_page_config(page_title="Tweet Classifier")
    st.header("Tweet Classifier Using Gemini LLM")

    # Initialize session state for classification history
    if 'classification_history' not in st.session_state:
        st.session_state['classification_history'] = []

    main_tweet = st.text_area("Main Tweet:", key="main_tweet")
    reply_tweet = st.text_area("Reply Tweet:", key="reply_tweet")
    classify_button = st.button("Classify Reply")
    reset_button = st.button("Reset")

    if classify_button and reply_tweet:
        classification = classify_tweet(reply_tweet)
        if classification:
            st.session_state['classification_history'].append((reply_tweet, classification))
            st.success(f"Classification: {classification}")

    if reset_button:
        st.session_state['classification_history'].clear()
        st.experimental_rerun()

    st.subheader("Classification History")
    for tweet, classification in st.session_state['classification_history']:
        st.text(f"Tweet: {tweet}\nClassification: {classification}")

if __name__ == "__main__":
    main()
