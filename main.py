import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Assistly Chatbot",
    page_icon=":medical_symbol:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling for chatbot interface
st.markdown("""
    <style>
    .stChatMessage { padding: 1em; border-radius: 10px; margin: 0.5em 0; }
    .userMessage { background-color: #e1f5fe; color: #00695c; }
    .assistantMessage { background-color: #f1f8e9; color: #33691e; }
    </style>
    """, unsafe_allow_html=True)

# Fetch the API key from environment variables
GOOGLE_API_KEY = os.getenv("AIzaSyAEofKOVx8eR6eB-13gIJndq3UYtqdYFjA")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to add predefined context to user queries
def get_response_with_context(user_prompt):
    context = """
    You are a healthcare assistant specializing in ART adherence and HIV prevention for mothers and children.
    Only respond to questions directly related to:
    - ART (Antiretroviral Therapy) adherence.
    - HIV prevention methods for pregnant women.
    - Health support strategies for HIV-positive mothers and children.
    
    Examples of appropriate questions:
    - "What are the benefits of ART adherence?"
    - "How can HIV-positive mothers reduce the risk of HIV transmission?"
    - "What support strategies are available for HIV-positive mothers?"

    Avoid answering questions that are not directly related to ART or HIV prevention.
    """
    prompt = f"{context}\n\nUser: {user_prompt}\nAssistant:"
    response = st.session_state.chat_session.send_message(prompt)
    return response

# Function to refine response if it seems too general
def refine_response_if_needed(response_text):
    if any(keyword in response_text.lower() for keyword in ["schedule", "appointments", "reminders", "productivity", "entertainment"]):
        refined_prompt = "Please refocus the response on ART adherence, HIV prevention, or health support for mothers and children."
        response = st.session_state.chat_session.send_message(refined_prompt)
        return response.text
    return response_text

# Function to translate roles for Streamlit's chat interface
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    return user_role

# Initialize chat session if not present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Chatbot title and description
st.title("🤖 Assistly - Improving HIV Treatment Completion for Pregnant Women")
st.subheader("💊 The best ART adherence chat tool 👶 Preventing mother-to-child HIV transmission 🩺 Health support strategies")

# Sidebar with chatbot purpose and quick tips
st.sidebar.header("About This Chatbot 💬")
st.sidebar.markdown("""
This chat tool supports efforts to improve ART (Antiretroviral Therapy) completion among HIV-positive pregnant women, a crucial step in preventing mother-to-child transmission of HIV.
Together, we’re empowering healthier futures for mothers and their children.
""")
st.sidebar.info("Empowering women and children effectively")

st.sidebar.header("Quick Tips 💡")
st.sidebar.markdown("""
- **ART Adherence**: Stick to your ART schedule to reduce the risk of HIV transmission.
- **Pregnancy and HIV**: Early ART treatment during pregnancy is crucial for reducing transmission to the baby.
- **Healthcare Support**: Reach out to local health clinics for ART supplies and counseling.
""")

# Display chat history
if not st.session_state.chat_session.history:
    with st.chat_message("assistant"):
        st.markdown("Hello! I'm here to support ART adherence and provide guidance on preventing mother-to-child HIV transmission. Feel free to ask me anything about ART, health support, or HIV prevention strategies.")

for message in st.session_state.chat_session.history:
    message_role = translate_role_for_streamlit(message.role)
    css_class = "assistantMessage" if message_role == "assistant" else "userMessage"
    st.markdown(f'<div class="stChatMessage {css_class}">{message.parts[0].text}</div>', unsafe_allow_html=True)

# Input field for user’s message
user_prompt = st.chat_input("Ask about ART adherence, HIV prevention, or health support for mothers and children...")
if user_prompt:
    st.markdown(f'<div class="stChatMessage userMessage">{user_prompt}</div>', unsafe_allow_html=True)

    # Get the initial response with context
    gemini_response = get_response_with_context(user_prompt)
    
    # Refine the response if needed
    final_response = refine_response_if_needed(gemini_response.text)

    # Display the final response
    with st.chat_message("assistant"):
        st.markdown(f'<div class="stChatMessage assistantMessage">{final_response}</div>', unsafe_allow_html=True)
