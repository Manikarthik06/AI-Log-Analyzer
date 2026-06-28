import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
import os

print("Current working directory:", os.getcwd())

# Load parsed logs
df = pd.read_csv("parsed_logs.csv")

# Create text column
df["log_text"] = (
    df["service"].fillna("").astype(str) + " " +
    df["message"].fillna("").astype(str)
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="security_logs"
)

# Store logs
for i, text in enumerate(df["log_text"]):
    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(i)],
        documents=[text],
        embeddings=[embedding]
    )

print("All logs stored successfully in ChromaDB.")
print("Total logs stored:", len(df))