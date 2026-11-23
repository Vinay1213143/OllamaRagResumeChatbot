from langchain_community.document_loaders import PyPDFLoader

PDF_PATH = r"C:\Users\vinay\OneDrive\Desktop\ThinkQuotient Generative AI\Gen AI\OllamaRagResumeChatbot\documents\Vinay_Resume.pdf"
loader=PyPDFLoader(PDF_PATH)
documents=loader.load()
print("Number of pages:",len(documents))

for i,doc in enumerate(documents):
    print(f"\n---PAGE {i+1}---")
    print(doc.page_content[:1000])
    print("Metadata:",doc.metadata)