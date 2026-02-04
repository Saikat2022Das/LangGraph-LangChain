from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3.2:1b", streaming=True)

for chunk in llm.stream([HumanMessage(content="Explain gravity in one line")]):
    print(chunk.content, end="", flush=True)
