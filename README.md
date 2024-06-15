Certainly! Here is a README file for the provided code:

---

# Chat Model using Streamlit and Google Generative AI

This project implements a simple chat application using Streamlit and the Google Generative AI model. The chat application allows users to interact with an AI assistant, which responds to their queries in real-time. This application uses the `streamlit_chat` component for the chat interface and the `ChatGoogleGenerativeAI` model from the `langchain_google_genai` library for generating responses.

## Requirements

- Python 3.7 or higher
- Streamlit
- Streamlit Chat
- LangChain Google Generative AI
- itertools (standard library)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:

    ```bash
    pip install streamlit streamlit-chat langchain_google_genai
    ```

3. Add your Google API key to the Streamlit secrets:

    Create a file named `secrets.toml` in the `.streamlit` directory:

    ```plaintext
    [secrets]
    API_KEY = "your_google_api_key_here"
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to interact with the chat application.

## Code Overview

### Imports

- `itertools.zip_longest`: To handle the pairing of input and response histories.
- `streamlit as st`: Streamlit library for building the web app.
- `from streamlit_chat import message`: To display chat messages.
- `from langchain_google_genai import ChatGoogleGenerativeAI`: To use Google's Generative AI model.
- `from langchain.schema import SystemMessage, HumanMessage, AIMessage`: To format chat messages.

### Configuration

- `st.set_page_config(page_title="Chat_Model")`: Sets the page title.
- `api_key = st.secrets["API_KEY"]`: Retrieves the API key from Streamlit secrets.

### Initializing the Chat Model

```python
chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
```

### Session State Initialization

- `st.session_state['prompt']`: Stores the current user prompt.
- `st.session_state['response']`: Stores the AI responses.
- `st.session_state['input_history']`: Stores the history of user inputs.

### User Input Handling

- `submit()`: Handles the submission of user input.

### Layout

- Sidebar with introduction and instructions.
- Fixed text input at the bottom for user queries.

### Message Handling

- `MakingLists()`: Creates a list of messages from the user and AI history.
- `generate_response()`: Generates a response using the chat model.

### Main Logic

- Appends user queries and AI responses to the session state.
- Displays the chat history using `streamlit_chat.message`.

## Additional Information

This project does not rely on libraries like Langchain, LLamaIndex, or Haystack for the alternative implementation. Instead, it directly utilizes the `langchain_google_genai` library for model interaction.

## Contact

For any questions or issues, please contact [Your Name] at sadiakanwal.9502@gmail.com.

---
