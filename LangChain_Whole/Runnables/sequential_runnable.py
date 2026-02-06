from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate


from langchain_core.runnables import RunnableSequence

prompt = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ["topic"]
)

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.3
)

chain = RunnableSequence(
    prompt, llm
)

print(chain.invoke({"topic": "chickens crossing the road"}))

print("----------------------------")
print('\n')

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain2 = RunnableSequence(
    prompt,
    llm,        
    parser
)

print(chain2.invoke({"topic": "chickens crossing the road"}))