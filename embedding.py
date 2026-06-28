import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load parsed logs
df = pd.read_csv("parsed_logs.csv")

# Create text representation of each log
df["log_text"] = (
    df["service"].fillna("").astype(str) + " " +
    df["message"].fillna("").astype(str)
)

# Load embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert logs to list
texts = df["log_text"].tolist()

# Generate embeddings
print("Generating embeddings...")
embeddings = model.encode(
    texts,
    show_progress_bar=True
)

# Save embeddings
np.save("log_embeddings.npy", embeddings)

# Save log text for future reference
df[["log_text"]].to_csv("log_texts.csv", index=False)

# Summary
print("\n===== EMBEDDING REPORT =====")
print("Total Logs:", len(texts))
print("Number of Embeddings:", len(embeddings))
print("Embedding Dimension:", len(embeddings[0]))
print("\nEmbeddings saved to: log_embeddings.npy")
print("Log texts saved to: log_texts.csv")