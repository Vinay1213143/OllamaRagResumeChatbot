from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
DB_PATH="chroma_db"
EMBEDDINIG_MODEL="nomic-embed-text"

embeddings=OllamaEmbeddings(
    model=EMBEDDINIG_MODEL
)

vector_db=Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

question="Which skills are mentioned in resume?"

result=vector_db.similarity_search(question,
                                   k=3)

print("QUESTION:")
print(question)

for i , doc in enumerate(result):
    print(f"\n---RESULT {i+1}---")
    print(doc.page_content)
    print("Metadata:",doc.metadata)