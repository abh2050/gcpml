import tkinter as tk
import tkinter.font as tkfont
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk
import openai
import threading
from queue import Queue
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

# Create a queue for storing classification tasks
task_queue = Queue()

# Worker function to classify tweets in the background
def worker():
    while True:
        # Get a tweet from the queue
        tweet_text = task_queue.get()

        # Perform classification
        classification = classify_tweet(tweet_text)

        # Safely update the UI with the result
        root.after(0, update_ui, tweet_text, classification)

        # Mark the task as completed
        task_queue.task_done()

def update_ui(tweet_text, classification):
    # Update the UI with the classification result for the given tweet text
    classification_label.config(text=f"Tweet: {tweet_text}\nClassification: {classification}")

# Function to handle the classify button click
def on_classify():
    main_tweet = main_tweet_entry.get("1.0", "end-1c")
    reply_tweet = reply_tweet_entry.get("1.0", "end-1c")

    if main_tweet and reply_tweet:
        # Add task to the queue
        task_queue.put(reply_tweet)
    else:
        messagebox.showwarning("Warning", "Please enter both a main tweet and a reply.")

# Create worker threads
for _ in range(5):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

# Function to close the application
def on_exit():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Tweet Classifier")
root.geometry("500x400")  # Width x Height
root.minsize(500, 400)    # Minimum size of the window
root.config(bg="#f0f0f0")

# Set a font style
fontStyle = tkfont.Font(family="Lucida Grande", size=12)

# Image and label setup ...

# Set a colored background for the main window and frames
background_color = "#ADD8E6"

# Main frame for content
main_frame = tk.Frame(root, padx=10, pady=10, bg=background_color)
main_frame.pack(expand=True, fill=tk.BOTH)

# Frame for the main tweet input
main_tweet_frame = tk.Frame(main_frame, pady=5, bg=background_color)
main_tweet_frame.pack(fill=tk.BOTH)
tk.Label(main_tweet_frame, text="Main Tweet:", font=fontStyle, bg=background_color).pack(anchor="w")
main_tweet_entry = tk.Text(main_tweet_frame, height=5, width=40, font=fontStyle)
main_tweet_entry.pack(fill=tk.BOTH, expand=True)

# Frame for the reply tweet input
reply_tweet_frame = tk.Frame(main_frame, pady=5, bg=background_color)
reply_tweet_frame.pack(fill=tk.BOTH)
tk.Label(reply_tweet_frame, text="Reply Tweet:", font=fontStyle, bg=background_color).pack(anchor="w")
reply_tweet_entry = tk.Text(reply_tweet_frame, height=5, width=40, font=fontStyle)
reply_tweet_entry.pack(fill=tk.BOTH, expand=True)

# Frame for buttons
button_frame = tk.Frame(main_frame, pady=5, bg=background_color)
button_frame.pack(fill=tk.X)

# Button sizes and font
buttonWidth = 15  # Width of the buttons
buttonHeight = 2  # Height of the buttons

# Classify button
classify_btn = tk.Button(button_frame, text="Classify Reply", command=on_classify, font=fontStyle, width=buttonWidth, height=buttonHeight)
classify_btn.pack(side=tk.LEFT, padx=5)

# Exit button
exit_btn = tk.Button(button_frame, text="Exit", command=on_exit, font=fontStyle, width=buttonWidth, height=buttonHeight)
exit_btn.pack(side=tk.RIGHT, padx=5)

# Reset button
reset_btn = tk.Button(button_frame, text="Reset", font=fontStyle, width=buttonWidth, height=buttonHeight)
reset_btn.pack(side=tk.LEFT, padx=5)

def reset_entries():
    main_tweet_entry.delete("1.0", tk.END)
    reply_tweet_entry.delete("1.0", tk.END)

reset_btn.config(command=reset_entries)

# Label to display classification results
classification_label = tk.Label(main_frame, font=fontStyle, bg=background_color)
classification_label.pack()

# Start the GUI event loop
root.mainloop()
