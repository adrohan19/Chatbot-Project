# PDF ChatBot

The PDF ChatBot is an interactive conversational agent that parses uploaded PDF documents to answer user queries in real-time. Leveraging natural language processing, it is capable of extracting and presenting information succinctly from the provided documents.

## Installation

Follow these steps to set up the PDF ChatBot on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adrohan19/pdf-chatbot.git
   ```
2. **Navigate to the project directory**:
  ```bash
  cd pdf-chatbot
  ```
3. **Set your OpenAI API key (replace 'YOUR_API_KEY' with your actual key)**:
   ```bash
   export OPENAI_API_KEY='YOUR_API_KEY'
   ```
## Usage

To launch the PDF ChatBot, execute the following command:
```bash
streamlit run chatbot.py
```
This will start the Streamlit server, and the application should open in your default web browser. If it does not, you can manually access it by navigating to http://localhost:8501 in your browser.
