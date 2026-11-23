from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

PDF_PATH = r"C:\Users\vinay\OneDrive\Desktop\ThinkQuotient Generative AI\Gen AI\OllamaRagResumeChatbot\documents\Vinay_Resume.pdf"

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Original pages:", len(documents))
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:10]):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk.page_content)
    print("Metadata:", chunk.metadata)
