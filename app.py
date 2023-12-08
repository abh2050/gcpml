import streamlit as st
import openai
from key import api_key  # Import your API key from a separate file

# Set your OpenAI API key
openai.api_key = api_key

# Define classification examples
classification_examples = [
    {"label": "Non Spam", "text": "This is a relevant tweet."},
    {"label": "Spam", "text": "Buy now! Special offer!"}
]

# Define the tweet classification function
def classify_tweet(tweet_text):
    prompt = "Classify the following tweet as 'Non Spam' or 'Spam':\n\n"
    for example in classification_examples:
        prompt += f"Tweet: \"{example['text']}\"\nClassification: {example['label']}\n"
    prompt += f"Tweet: \"{tweet_text}\"\nClassification:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=40
    )

    return response.choices[0].text.strip()

# Streamlit app layout
def main():
    st.title("Tweet Classifier")

    # Text input for main tweet and reply
    main_tweet = st.text_area("Main Tweet:")
    reply_tweet = st.text_area("Reply Tweet:")

    # Button to classify tweet
    if st.button("Classify Reply"):
        if main_tweet and reply_tweet:
            classification = classify_tweet(reply_tweet)
            st.success(f"Classification: {classification}")
        else:
            st.warning("Please enter both a main tweet and a reply.")

    # Button to reset the input fields
    if st.button("Reset"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
