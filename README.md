![image](https://miro.medium.com/v2/resize:fit:1400/1*NO_n8kfHA9FzTJRZV8wPXA.jpeg)

![Python 3.8](https://img.shields.io/badge/Python-3.8-blue?style=flat&logo=python&logoColor=white&link=https://www.python.org/)
![OpenAI API 0.28](https://img.shields.io/badge/OpenAI_API_0.28-FF9900?style=flat&logo=openai&logoColor=white&link=https://openai.com/api/)
![Functions Framework 3.x](https://img.shields.io/badge/Functions_Framework_3.x-FF69B4?style=flat&logo=google-cloud&logoColor=white&link=https://cloud.google.com/functions)
![Flask 1.1.4](https://img.shields.io/badge/Flask_1.1.4-000000?style=flat&logo=flask&logoColor=white&link=https://flask.palletsprojects.com/)
![Jinja2 2.11.3](https://img.shields.io/badge/Jinja2_2.11.3-B41717?style=flat&logo=jinja&logoColor=white&link=https://jinja.palletsprojects.com/)
![MarkupSafe 1.1.1](https://img.shields.io/badge/MarkupSafe_1.1.1-9CF?style=flat&logo=python&logoColor=white&link=https://palletsprojects.com/p/markupsafe/)
![Deployed on GCP](https://img.shields.io/badge/Deployed_on_GCP-blue?style=flat&logo=google-cloud&logoColor=white&link=https://cloud.google.com/)
![Dockerized](https://img.shields.io/badge/Dockerized-2496ED?style=flat&logo=docker&logoColor=white&link=https://www.docker.com/)



# Tweet Classifier: User Guide and Technical Documentation

## Table of Contents
1. [Introduction](#1-introduction)
2. [System Requirements](#2-system-requirements)
3. [Installation and Deployment Guide](#3-installation-and-deployment-guide)
    - 3.1. [Local Installation](#31-local-installation)
    - 3.2. [Docker Deployment](#32-docker-deployment)
    - 3.3. [Cloud Deployment](#33-cloud-deployment)
4. [User Guide](#4-user-guide)
    - 4.1. [Main Features](#41-main-features)
    - 4.2. [Walk-through for Main Scenario](#42-walk-through-for-main-scenario)
    - 4.3. [Additional Usage Scenarios](#43-additional-usage-scenarios)
5. [API Documentation](#5-api-documentation)
6. [Troubleshooting and FAQ](#6-troubleshooting-and-faq)

---

## 1. Introduction
**Name:** Tweet Classifier Using OpenAI 
**Description:**  
Tweet Classifier is a software application designed to classify tweets as either 'Non Spam' or 'Spam.' This tool is particularly useful for social media managers, digital marketers, and individuals who manage multiple Twitter accounts. It leverages the OpenAI API to analyze tweet content and provide a classification based on pre-defined examples.

**Intended Users:**
- Social Media Managers
- Digital Marketers
- Twitter Account Administrators
- Individuals interested in filtering spam content on Twitter

---

## 2. System Requirements
- Python 3.x
- Libraries: tkinter, PIL, openai
- Docker (for Docker deployment)
- Google Cloud account and SDK (for Cloud deployment)
- Operating System: Cross-platform (Windows, macOS, Linux)

---

## 3. Installation and Deployment Guide

### 3.1. Local Installation
**Prerequisites:**
- Python 3.x installed

**Installation Steps:**
1. Ensure Python 3.x is installed on your system.
2. Install necessary Python libraries:
   - Run `pip install pillow openai`
3. Obtain an API key from OpenAI and save it in a file named `key.py` in the format: `api_key = "Your_API_Key"`
4. Download the Tweet Classifier codebase.

**Deployment:**
- Run the application by executing the Python script: `main.py`
- The GUI window should open, ready for use.

### 3.2. Docker Deployment
**Prerequisites:**
- Docker installed on the system

**Steps for Docker Deployment:**
1. Build the Docker Image:
   - Navigate to the directory containing the Dockerfile.
   - Run the command: `docker build -t tweet-classifier .`
   - This builds a Docker image named `tweet-classifier` from the Dockerfile.
2. Run the Container:
   - Once the image is built, start the container using: `docker run -p 8080:8080 tweet-classifier`
   - This command maps port 8080 of the container to port 8080 on the host machine.
3. Accessing the Application:
   - The application should now be running inside the Docker container and can be accessed through the host machine's browser or command line interface.

### 3.3. Cloud Deployment (Google Cloud Functions)
**Preparing the Function:**
- Update the Python script...
- Include the `key.py` file...

**Setting Up Google Cloud Storage:**
**Prerequisites:**
- Google Cloud account
- Google Cloud SDK installed and configured
- Access to Google Cloud Storage

**Steps for Cloud Deployment:**
1. **Prepare the Cloud Function:**
   - Update the provided Python script to handle HTTP requests for classifying tweet replies.
   - Ensure the `key.py` file with your OpenAI API key is included.
   
2. **Setting Up Google Cloud Storage:**
   - Create two buckets in Google Cloud Storage: `inputtweet` and `outputtweet`.
   - Configure the buckets as per your data privacy and access requirements.

3. **Deploying the Function:**
   - Navigate to the Google Cloud Console.
   - Go to the Cloud Functions section and create a new function.
   - Set the runtime to Python 3.8 and the entry point to `classify_reply_http`.
   - Upload your code or connect to the source repository containing your function.
   - Set the trigger type to HTTP and deploy the function.

**Function URL:**
- Once deployed, the function will be accessible via an HTTPS URL (e.g., `https://us-west1-spheric-bloom-350617.cloudfunctions.net/tweet`)

---

## 4. User Guide
![sequence](https://github.com/abh2050/gcpml/blob/main/Sequence.png)

### 4.1. Main Features

**Tweet Classification:**
- Functionality (All Platforms): The primary function of Tweet Classifier is to analyze tweets and categorize them as either 'Non Spam' or 'Spam' using AI technology.
- Local/Docker/Cloud: This feature is consistent across local, Docker, and cloud deployments, offering reliable classification regardless of the deployment method.
- Usage: Users input the text of a tweet, and the system processes this input to provide a classification.

**User Interface (Local and Docker Deployments):**
- Design: A straightforward and intuitive graphical user interface (GUI) designed using tkinter.
- Components: Includes text boxes for entering tweets, buttons for classification, resetting, and exiting.
- Local/Docker: Accessible in local and Docker deployments where the GUI is directly interacted with.

**Cloud Functionality (Cloud Deployment):**
- Design: In cloud deployment, the application functions as a backend service.
- Interaction: Users interact with the service through HTTP requests, typically via an API call or a frontend interface that communicates with the cloud function.
- Usage: The cloud function reads tweet data from a designated storage bucket, processes it, and writes the results to another bucket.

**Batch Analysis (Local and Docker Deployments):**
- Functionality: Processing and classification of tweets upon submission.
- Advantage: Quick feedback is essential for managing social media content in a timely manner.

**Reset Functionality (Local and Docker Deployments):**
- Purpose: Allows users to clear input fields quickly to classify new tweets.
- User Experience: Streamlines the process of analyzing multiple tweets.

**Batch Processing (Cloud Deployment):**
- Functionality: The cloud deployment batch processes the tweet classification process using a trigger.
- Workflow: Reads tweets from an input bucket, classifies them, and outputs the results to an output bucket.
- Advantage: Suitable for bulk processing and integration into larger automated systems.

### 4.2. Walk-through for Main Scenario

![process](https://github.com/abh2050/gcpml/blob/main/board-hilarious-farceur.jpg)

**Local Deployment:**

**Starting the Application:**
1. Navigate to the folder containing the Tweet Classifier script.
2. Run the application by executing the command: `python tweet_classifier.py`.
3. The GUI window of the Tweet Classifier will open.

**Using the Application:**
1. In the 'Main Tweet' text box, enter the content of the tweet you want to classify.
2. In the 'Reply Tweet' text box, enter the reply to the tweet for classification.
3. Click on the 'Classify Reply' button to submit the tweet for classification.

**Docker Deployment:**

**Starting the Application:**
- Ensure the Docker container is built and running. Use the command: `docker run -p 8080:8080 tweet-classifier`.
- Access the application's GUI if it's configured to be accessible via a web interface or through a Docker container's display output.

**Using the Application:**
- The steps for entering tweet text and classifying it remain the same as in the local deployment.

**Walk-through for Main Scenario (Cloud Deployment)**

**Triggering the Function Manually:**

**Uploading Tweets for Classification:**
1. **Prepare Your Tweet Data:**
   - Format your tweet data in JSON. Each tweet should be a separate JSON object in the file.
   - Example format:
     ```json
     {
      "tweet": "Here is the content of the tweet.",
      "reply": "This is a reply to the above tweet."
     }
     ```

2. **Accessing Google Cloud Storage:**
   - Navigate to the Google Cloud Console.
   - Go to your storage buckets.

**Uploading Data to `inputtweet` Bucket:**
- Select the `inputtweet` bucket.
- Upload your JSON file containing the tweet data.

**Manually Triggering the Cloud Function:**
- Access the Cloud Function:
  - In the Google Cloud Console, go to the Cloud Functions section.
  - Find the Tweet Classifier function.
- **Trigger the Function:**
  - Trigger the function manually. This can typically be done through the Google Cloud Console, often with a 'Run' or 'Test function' button.
  - Ensure that the function is configured to read from the `inputtweet` bucket upon execution.

**Viewing the Results:**
- **Retrieving Classification Results:**
- **Accessing the `outputtweet` Bucket:**
- After the cloud function processes the tweet data, the results are stored in the `outputtweet` bucket.
- Navigate to the `outputtweet` bucket in Google Cloud Storage.
- **Downloading the Results:**
  - Look for a file named similarly to your input file but prefixed with 'classified_'.
  - Download this file to view the classification results.
  - The result file will contain the original tweet data along with an added field indicating the classification ('Spam' or 'Not Spam').

### 4.3. Additional Usage Scenarios

**Scenario 1: Resetting Entries (Local and Docker Deployments)**

**Steps for Resetting Entries:**
- **Using the Reset Button:**
  - In the GUI, locate the 'Reset' button, typically near the 'Classify' button.
  - Click on the 'Reset' button to clear all text fields, including 'Main Tweet' and 'Reply Tweet' inputs.
  - The application is now ready for new entries without manually deleting old ones.

**Scenario 2: Exiting the Application (Local and Docker Deployments)**

**Steps for Exiting the Application:**
- **Locating the Exit Button:**
  - Find the 'Exit' button in the GUI, usually at the bottom or near the other buttons.
  - Click the 'Exit' button to safely close the application and terminate the session.

**Scenario 3: Triggering Cloud Function (Cloud Deployment)**

**Steps for Manually Triggering the Function:**
- **Accessing the Function:**
  - Navigate to the Cloud Functions section in the Google Cloud Console.
  - Find and select the Tweet Classifier function.
- **Triggering the Function:**
  - Use the provided interface to manually trigger the function.
  - Ensure that the function is set to read from the `inputtweet` bucket.

**Scenario 4: Monitoring Function Execution (Cloud Deployment)**

**Steps for Monitoring:**
- **Accessing Logs:**
  - In the Google Cloud Console, navigate to the 'Logging' section.
  - Filter logs by the name of your function to see its execution history and any runtime messages.
- **Analyzing Logs:**
  - Review the logs for information about function execution, such as start and end times, errors, or warnings.

## 5. API Documentation

<details>
<summary><strong>Endpoint:</strong></summary>

- **URL:** The API endpoint for the Tweet Classifier cloud function.
- **Example:** `https://us-west1-spheric-bloom-350617.cloudfunctions.net/tweet`
- **Method:** POST 
</details>

<details>
<summary><strong>Request Format:</strong></summary>

- **Content-Type:** `application/json`
- **Body Structure:** The request should contain tweet data in JSON format.
- **Example Request Body:**
  ```json
  {
   "tweet": "Sample tweet content.",
   "reply": "Sample reply to the tweet."
  }
  ```
</details>

<details>
<summary><strong>Response Format:</strong></summary>

- **Content-Type:** `application/json`
- **Response Structure:** The response will include the original tweet data along with the classification result.
- **Example Response:**
  ```json
  {
   "tweet": "Sample tweet content.",
   "reply": "Sample reply to the tweet.",
   "classification": "Non Spam"
  }
  ```
</details>

<details>
<summary><strong>Usage Example:</strong></summary>

- **Sample cURL Command:**
  ```bash
  curl -X POST -H "Content-Type: application/json"   -d '{"tweet": "Sample tweet content.", "reply": "Sample reply to the tweet."}'   "https://us-west1-spheric-bloom-350617.cloudfunctions.net/tweet"
  ```

- **Python Example:**
  ```python
  import requests
  import json

  data = {
   "tweet": "Sample tweet content.",
   "reply": "Sample reply to the tweet."
  }

  response = requests.post(
   "https://us-west1-spheric-bloom-350617.cloudfunctions.net/tweet",
   data=json.dumps(data),
   headers={"Content-Type": "application/json"}
  )

  print(response.json())
  ```
</details>

---

## 6. Troubleshooting and FAQ

<details>
<summary><strong>Common Issues:</strong></summary>

- **Issue 1: Unable to Connect to OpenAI API**
  
  **Solution:**
  - Verify that your OpenAI API key is correctly set in the `key.py` file.
  - Check your internet connection.
  - Ensure that there are no restrictions blocking access to the OpenAI API.

- **Issue 2: Docker Container Not Starting**

  **Solution:**
  - Ensure Docker is correctly installed and running on your system.
  - Check the Docker container logs for any error messages: `docker logs [container_name]`.
  - Verify that all necessary files are included in the Docker build context.

- **Issue 3: Cloud Function Not Triggering**

  **Solution:**
  - Confirm that the cloud function is deployed correctly with the correct trigger settings.
  - Make sure that the `inputtweet` bucket exists and you have the necessary permissions to access it.
  - Check Google Cloud Function logs for any execution errors or warnings.
</details>

<details>
<summary><strong>Frequently Asked Questions:</strong></summary>

## Frequently Asked Questions (FAQ)

### Q1: How can I update the classification examples used by the application?
**A:** For local and Docker deployments, modify the `classification_examples` list in the Python script. For the cloud deployment, update the examples in the cloud function before redeployment.

### Q2: What should I do if the classification results are not accurate?
**A:** The accuracy of classifications largely depends on the training of the OpenAI model and the examples provided. You can improve accuracy by refining the examples or retraining the model with more data.

### Q3: Can the Tweet Classifier handle multiple languages?
**A:** Currently, the Tweet Classifier is optimized for English. However, it can be adapted to other languages by using a multilingual model from OpenAI and adjusting the classification examples accordingly.

### Q4: Is there a limit to the number of tweets that can be classified at once?
**A:** For local and Docker deployments, the limit depends on the system's resources. For cloud deployments, the limit is determined by the Google Cloud Function's quotas and limits.

### Q5: How secure is the Tweet Classifier in handling sensitive data?
**A:** The Tweet Classifier does not store tweet data permanently. However, ensure that your OpenAI API key and cloud credentials are securely managed. For sensitive data, consider implementing additional encryption and security measures.

### Q6: Can I integrate the Tweet Classifier with other social media platforms?
**A:** While the current version is designed for Twitter, the application can be modified to work with other social media platforms by adjusting the input and output formats and API integrations.

### Q7: How can I contribute to the development of the Tweet Classifier?
**A:** Contributions can be made via the project's GitHub repository. You can fork the repository, make changes, and submit a pull request for review.

### Q8: Are there any costs associated with using the Tweet Classifier?
**A:** While the software is free, using the OpenAI API and cloud services (if deployed on Google Cloud) may incur costs. Check the respective service providers for pricing details.

### Q9: How do I report bugs or request features?
**A:** Bugs can be reported, and feature requests can be made through the project's issue tracker on GitHub or by contacting the development team directly.

### Q10: Is there any user support or community forum for the Tweet Classifier?
**A:** User support is primarily provided through the GitHub repository. Additionally, you can join community forums or discussion groups related to the project for more interactive support.

</details>


