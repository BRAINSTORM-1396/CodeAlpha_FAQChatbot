import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI FAQ Chatbot")
st.write("Ask me a question about our institution!")

# Frequently asked questions and answers
faqs = [
    {
        "question": "What courses do you offer?",
        "answer": "We offer Computer Engineering, Electrical Engineering, and Information Technology."
    },
    {
        "question": "How can I apply for admission?",
        "answer": "You can apply by completing the institution's admission application form."
    },
    {
        "question": "What are your opening hours?",
        "answer": "Our fictional institution operates from Monday to Friday, 8 AM to 5 PM."
    },
    {
        "question": "Where are you located?",
        "answer": "Our fictional institution is located in Kumasi, Ghana."
    },
    {
        "question": "How can I contact you?",
        "answer": "You can contact the administration through the institution's official email or telephone number."
    },
    {
        "question": "Do you offer scholarships?",
        "answer": "Scholarships may be available to eligible students. Contact the admissions office for details."
    },
    {
        "question": "How much are the school fees?",
        "answer": "Fees depend on the programme. Please contact the admissions office for the current fee schedule."
    },
    {
        "question": "When does admission open?",
        "answer": "Admission dates vary. Please check the institution's official announcements."
    }
]

# Prepare the FAQ questions for text matching
faq_questions = [faq["question"] for faq in faqs]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)

# Store the conversation in the Streamlit session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 Ask me anything about our institution."
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept a question from the user
user_question = st.chat_input("Type your question here...")

if user_question:
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    # Convert the user's question into a numerical representation
    user_vector = vectorizer.transform([user_question])

    # Find the closest matching FAQ
    similarities = cosine_similarity(user_vector, faq_vectors)[0]
    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    # Respond only when the match is sufficiently strong
    if best_score >= 0.25:
        answer = faqs[best_match_index]["answer"]
    else:
        answer = (
            "Sorry, I couldn't find a suitable answer. "
            "Please try asking about courses, admissions, fees, "
            "scholarships, location, or opening hours."
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)