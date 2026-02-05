from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3.2:1b",
    streaming = True
)

# Create Prompt Template
prompt = PromptTemplate(
    input_variables=["context"],
    template="Suggest a catchy blog title for the following content: {context}"
)

topic = input("Enter the topic for the blog: ")

format_prompt = prompt.format(context=topic)

blogtitle = llm.invoke(format_prompt)

print(f"Suggested Blog Title: {blogtitle}")