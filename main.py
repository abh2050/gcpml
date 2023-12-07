#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import tkinter.font as tkfont
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk
import openai
import threading
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

# Function to handle the classify button click
def on_classify():
    main_tweet = main_tweet_entry.get("1.0", "end-1c")
    reply_tweet = reply_tweet_entry.get("1.0", "end-1c")

    if main_tweet and reply_tweet:
        # Use threading to perform classification in the background
        thread = threading.Thread(target=classify_and_show_result, args=(reply_tweet,))
        thread.start()
    else:
        messagebox.showwarning("Warning", "Please enter both a main tweet and a reply.")

# Function to perform classification and show the result
def classify_and_show_result(tweet_text):
    classification = classify_tweet(tweet_text)
    messagebox.showinfo("Classification Result", f"Reply Classification: {classification}")

# Function to close the application
def on_exit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Tweet Classifier")
root.geometry("500x400")  # Width x Height
root.minsize(500, 400)    # Minimum size of the window
root.config(bg="#f0f0f0") # Background color

# Set a font style
fontStyle = tkfont.Font(family="Lucida Grande", size=12)

# Uncomment and correct this section for image display
logo_image = Image.open("pic.png")  # Replace with your actual logo path
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)  # Resize to 100x100 pixels or your desired size
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="#f0f0f0")
logo_label.pack(pady=10)

# Set a colored background for the main window and frames
background_color = "#ADD8E6"  # Light blue color, you can choose your preferred color
root.config(bg=background_color)

# Main frame for content
main_frame = tk.Frame(root, padx=10, pady=10, bg=background_color)
main_frame.pack(expand=True, fill=tk.BOTH)

# Frame for the main tweet input
main_tweet_frame = tk.Frame(main_frame, pady=5, bg=background_color)
main_tweet_frame.pack(fill=tk.BOTH)
tk.Label(main_tweet_frame, text="Main Tweet:", font=fontStyle, bg="#f0f0f0").pack(anchor="w")
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

# Classify button
classify_btn = tk.Button(button_frame, text="Classify Reply", command=on_classify, font=fontStyle)
classify_btn.pack(side=tk.LEFT, padx=5)

# Exit button
exit_btn = tk.Button(button_frame, text="Exit", command=on_exit, font=fontStyle)
exit_btn.pack(side=tk.RIGHT, padx=5)

def reset_entries():
    main_tweet_entry.delete("1.0", tk.END)
    reply_tweet_entry.delete("1.0", tk.END)

# Reset button
reset_btn = tk.Button(button_frame, text="Reset", command=reset_entries, font=fontStyle)
reset_btn.pack(side=tk.LEFT, padx=5)

# Start the GUI event loop
root.mainloop()


# In[ ]:




