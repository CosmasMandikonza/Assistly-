

---

# Assistly - Improving HIV Treatment Completion for Pregnant Women

Welcome to **Assistly**, a specialized chatbot built with Google's Gemini-Pro and Streamlit, designed to support ART (Antiretroviral Therapy) adherence among HIV-positive pregnant women. Assistly provides crucial guidance for preventing mother-to-child HIV transmission and offers health support strategies for mothers and children. This tool is part of an initiative to improve health outcomes through accessible digital healthcare support.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

Assistly is a healthcare assistant chatbot that:
- **Focuses on ART adherence**: Provides reminders and information on the importance of ART (Antiretroviral Therapy) adherence for HIV-positive pregnant women.
- **Supports HIV prevention**: Guides users on best practices to reduce the risk of mother-to-child transmission of HIV.
- **Offers health support strategies**: Suggests tips for health and wellness for both mothers and children, emphasizing the importance of early intervention and regular check-ups.

By leveraging Google's Gemini-Pro AI and the simplicity of Streamlit, Assistly delivers a user-friendly platform with specific, actionable information to support health improvement for at-risk populations.

## Features

- 🧠 **AI-Powered Chatbot**: Uses Google Gemini-Pro to answer specific health-related questions around ART adherence, HIV prevention, and health support for mothers and children.
- 💬 **Real-Time Conversation**: Engage in live, interactive conversations with the chatbot for real-time advice and information.
- 🌍 **Health Support Focus**: Delivers guidance tailored to HIV-positive pregnant women, providing targeted advice to improve ART completion and overall health.
- 📅 **Reminders & Tips**: Offers tips on ART adherence, prevention strategies, and health check-ups to ensure well-being for both mother and child.

## Getting Started

To get a copy of Assistly running on your local machine for development and testing purposes, follow the setup instructions below.

### Prerequisites

- Python 3.7+
- [Google Cloud API Key](https://console.developers.google.com/)
- [Streamlit](https://streamlit.io/)

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/CosmasMandikonza/Assistly
    cd Assistly
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Setup:**
   Create a `.env` file in the root directory and add your Google API key:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run main.py
   ```

2. **Interact with the Chatbot:**
   - Open the local server link provided in the terminal to start using Assistly.
   - Type your queries related to ART adherence, HIV prevention, or health support strategies in the chatbox, and receive relevant information in real-time.

## Project Structure

```plaintext
Assistly/
├── .env                    # Environment variables
├── main.py                 # Main application script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .venv/                  # Virtual environment (not in repo)
```

## Technologies Used

- **[Google Gemini-Pro](https://cloud.google.com/)**: A language model from Google Cloud used to provide intelligent, context-aware responses.
- **[Streamlit](https://streamlit.io/)**: A Python library for building interactive web applications easily.
- **Python 3.7+**: The core programming language used for building the backend of the chatbot.

## Contributing

Contributions are welcome! If you'd like to improve the functionality, add new features, or fix issues, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

