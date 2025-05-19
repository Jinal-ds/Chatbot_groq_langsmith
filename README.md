# 🤖 Chatbot with Groq, LangGraph & Langsmith

A fast and intelligent chatbot built using Groq models, structured with LangGraph, and monitored via Langsmith. This project leverages Groq's powerful inference API, integrates Langsmith for tracing/debugging, and uses LangGraph to structure conversations as graphs.

## 🚀 Features

- Groq LLM integration (Mixtral, LLaMA, etc.)
- Modular conversation flow using LangGraph
- Tracing & observability with Langsmith
- Clean, API-based architecture
- Easy to extend and debug

## 🛠 Tech Stack

- **LLM**: Groq API
- **Graph Structure**: LangGraph
- **Monitoring**: Langsmith
- **Language**: Python

🧠 Project Structure
├── main.py               # Streamlit UI & logic
├── chatbot.py     # LangGraph structure
├── chatbot.ipynb
├── requirements.txt     # Dependencies
└── README.md
💬 Example Interaction
You: Who won the last World Cup?
Bot: Argentina won the 2022 FIFA World Cup after beating France in a dramatic final!
🔍 Langsmith Integration
All chatbot interactions and graph traces are logged at Langsmith. Use it to debug the graph, inspect model outputs, and monitor performance.
📄 License
This project is released under the MIT License.

