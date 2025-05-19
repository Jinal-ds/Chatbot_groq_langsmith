import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
 # Uncomment if needed

# Set your keys (replace with your real or environment-managed keys)
groq_api_key = '' #your api keys
langsmith = ''

os.environ["LANGCHAIN_API_KEY"] = langsmith
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "CourseLanggraph"

# Define the state
class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# Define LLM and chatbot function
llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

# Build the graph
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

# Stream response function to be used in Streamlit or CLI
def stream_chat_response(user_input):
    response = ""
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            message = value.get("messages")
            if hasattr(message, "content"):
                response += message.content
            elif isinstance(message, list):
                for msg in message:
                    if hasattr(msg, "content"):
                        response += msg.content
    return response.strip()
