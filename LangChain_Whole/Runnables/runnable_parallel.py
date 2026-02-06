from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence

from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}",
    input_variables=["topic"]
)

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.3
)

parser = StrOutputParser()

chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, llm, parser),
    "linkedin": RunnableSequence(prompt2, llm, parser)
})

print(chain.invoke({"topic": "Embedding vs Tokenization"}))
