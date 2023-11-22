#!/usr/bin/env python
# coding: utf-8


import openai
import random
import json

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'


# Define examples for the model to understand the classification context
classification_examples = [
    {"label": "Relevant", "text": "This is a relevant tweet."},
    {"label": "Non-Relevant", "text": "This is a non-relevant tweet."},
    {"label": "Spam", "text": "Buy now! Special offer!"}
]


# Read tweets from the file and store them in a list
tweets = []
with open("tweet_reply.json", "r") as file:
    for line in file:
        tweet_data = json.loads(line)
        tweets.append(tweet_data)

# Randomly select 3 main tweets and their corresponding replies
random_tweets = random.sample(tweets, 2)

# Print the selected main tweets and their replies
for tweet in random_tweets:
    main_tweet = tweet['main_tweet']
    reply = tweet['reply']

    # Print the main tweet and reply
    print(f"Main Tweet: '{main_tweet}'")
    print(f"Reply: '{reply}'")
    print()


# Function to classify a tweet
def classify_tweet(tweet_text):
    prompt = "Classify the following tweet as 'Relevant', 'Non-Relevant', or 'Spam':\n\n"
    for example in classification_examples:
        prompt += f"Tweet: \"{example['text']}\"\nClassification: {example['label']}\n"
    prompt += f"Tweet: \"{tweet_text}\"\nClassification:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=40
    )

    return response.choices[0].text.strip()


# Classify the selected tweets and print the results
for tweet in random_tweets:
    main_tweet = tweet['main_tweet']
    reply = tweet['reply']

    # Classify main tweet and reply
    main_tweet_label = classify_tweet(main_tweet)
    reply_label = classify_tweet(reply)

    # Print the classification results
    print(f"Main Tweet: '{main_tweet}'\nClassification: {main_tweet_label}\n")
    print(f"Reply: '{reply}'\nClassification: {reply_label}\n")

