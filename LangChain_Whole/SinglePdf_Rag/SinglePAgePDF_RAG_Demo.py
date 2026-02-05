## WORKFLOW ##
## PDF LOAD => SPLITS => EMBEDDINGS => VECTORSTORE => RETRIEVAL => LLM => STR OUTPUT PARSER ##


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import PromptTemplate


# -----------------------------
# 1. Load PDF
# -----------------------------
pdf_path = "/Users/saikat/Downloads/Saikat_IIT_Jammu.pdf"   # <-- put your PDF path here
loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"Loaded {len(documents)} pages from PDF")


# -----------------------------
# 2. Split into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
docs = text_splitter.split_documents(documents)

print(f"Split into {len(docs)} chunks")


# -----------------------------
# 3. Create embeddings + FAISS
# -----------------------------
embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = FAISS.from_documents(
    docs,
    embedding=embeddings
)


# -----------------------------
# 4. Create retriever
# -----------------------------
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


# -----------------------------
# 5. Load LLM
# -----------------------------
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0.3,
    streaming=True
)


# -----------------------------
# 6. Ask question loop
# -----------------------------
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an assistant answering questions from a PDF.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""
)

while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    retrieved_docs = retriever.invoke(query)

    context_text = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    formatted_prompt = prompt.format(
        context=context_text,
        question=query
    )

    # response = llm.invoke(formatted_prompt)

    print("\nAnswer:")
    for chunk in llm.stream(formatted_prompt):
        print(chunk.content, end="", flush=True)
    print("\n---------------------------------\n")
    print('----------------------------')
