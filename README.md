# FAQ Chatbot

## About the Project

This project is a simple FAQ chatbot developed using Python.
It allows users to type questions and receive answers from a
collection of frequently asked questions.

The main idea behind the project is to make it easier for users
to find answers without having to search through information
manually.

## What the Chatbot Can Do

- Accept questions from users.
- Search through a list of frequently asked questions.
- Identify a question that is similar to what the user entered.
- Display the answer associated with the closest matching question.
- Inform the user when it cannot find a suitable answer.

## Tools Used

The project was developed with the following tools:

- Python for the main program.
- Streamlit for the chatbot interface.
- Scikit-learn for text processing and question matching.

## How It Works

The chatbot has a collection of questions and their answers.
When a user enters a question, the program compares it with the
questions already stored in the system.

TF-IDF is used to represent the questions numerically, while
cosine similarity helps the program determine which stored
question is the closest match.

If the similarity score is high enough, the chatbot displays
the corresponding answer. Otherwise, it asks the user to try
another question.

## How to Run the Project

First, install the required Python packages:

    python -m pip install streamlit scikit-learn

Next, open a terminal in the project folder and run:

    python -m streamlit run app.py

The chatbot will open in a web browser.

## Testing

I tested the chatbot using questions about the available courses
and the admission process. It returned the expected answers.

I also entered a question unrelated to the information stored
in the chatbot. The program correctly displayed its fallback
response.

## Current Limitations

The chatbot can only answer questions covered by its stored
information. It may also fail to recognize some questions if
their wording differs significantly from the questions in its
database.

## Future Improvements

Possible improvements include adding more questions, improving
the matching process, and making the interface more interactive.