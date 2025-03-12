# Flask Chat App

This project is a simple Flask application that implements a ChatGPT-like chat window for user interaction with the OpenAI model. It allows users to communicate with the model through a web interface.

## Project Structure

```
flask-chat-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── index.html
├── .env
├── config.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-chat-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the application:**
   ```
   flask run
   ```

6. **Access the chat interface:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- Type your message in the chat window and press enter to send it.
- The assistant will respond based on the input provided.
- Ensure that your OpenAI API key is valid for the application to function correctly.

## License

This project is licensed under the MIT License.