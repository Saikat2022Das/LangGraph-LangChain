from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
# from dotenv import load_dotenv

# load_dotenv()
from langchain_community.llms import Ollama

Model = "llama3.2:1b"
llm = Ollama(model=Model)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages] # BaseMessage Includes human and assistant messages and other messages like tool messages.
    ###################################### add_messages is a reducer function, which is stored past conversation.

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)