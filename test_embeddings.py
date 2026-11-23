import ollama
MODEL="nomic-embed-text"

text="Employees are entitled 5-6 skills."

response=ollama.embeddings(
    model=MODEL,
    prompt=text
)

embedding=response["embedding"]

print("MODEL:",MODEL)
print("Embedding length:",len(embedding))
print("First 10 values:",embedding[:10])