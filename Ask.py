import pandas as pd
import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from langchain.schema import Document  # Correct import

# Load CSV data
data = pd.read_csv('students_data.csv')  # Replace with your CSV file

# Function to create embeddings from the CSV data
def create_embeddings(data):
    # Combine all rows into a single text
    combined_text = data.apply(lambda row: ' '.join(row.astype(str)), axis=1).tolist()

    # Convert texts into Document objects
    documents = [Document(page_content=text) for text in combined_text]

    # Check if FAISS index exists, if not, create one
    if os.path.exists("faiss_index"):
        vector_store = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    else:
        vector_store = FAISS.from_documents(documents, OpenAIEmbeddings())
        vector_store.save_local("faiss_index")

    return vector_store

# Initialize LangChain components
def initialize_chatbot():
    vector_store = create_embeddings(data)
    retriever = vector_store.as_retriever()
    llm = OpenAI()  # Use GPT model
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)
    return qa_chain

# Chatbot loop
def chat():
    qa_chain = initialize_chatbot()
    print("Hello! I'm your LangChain chatbot. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = qa_chain.run(user_input)
        print("Chatbot:", response)

if __name__ == '__main__':
    chat()
