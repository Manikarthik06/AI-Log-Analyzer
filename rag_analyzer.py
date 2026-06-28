import chromadb
from matplotlib import collections
from sentence_transformers import SentenceTransformer
import ollama
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "chroma_db")

print("=" * 60)
print("Working Directory:", os.getcwd())
print("Script Directory :", BASE_DIR)
print("Database Path    :", DB_PATH)

client = chromadb.PersistentClient(path="/Users/manikarthikgarlapati/Documents/vs code/AILA/chroma_db")

print("Collections Found:", client.list_collections())
print("=" * 60)

collection = client.get_collection("security_logs")

print("Current working directory:", os.getcwd())

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def ask_rag(user_question):

    try:
        # Connect to ChromaDB
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_PATH = os.path.join(BASE_DIR, "chroma_db")

        client = chromadb.PersistentClient(path=DB_PATH)

        # Load collection
        collections = client.list_collections()

        print("Collections:")
        for c in collections:
            print("Name:", c.name)

        collection = client.get_or_create_collection(name="security_logs")

        print("Collection Name:", collection.name)
        print("Document Count:", collection.count())

    except Exception as e:
        return f"Error loading ChromaDB collection: {e}"

    try:
        # Create query embedding
        query_embedding = model.encode(user_question).tolist()

        # Retrieve relevant logs
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        retrieved_logs = "\n".join(results["documents"][0])

        prompt = f"""
You are an experienced SOC (Security Operations Center) Analyst.

Generate a professional Cybersecurity Incident Report.

The report MUST contain:

1. Executive Summary

2. Severity
(Low / Medium / High / Critical)

3. Attack Analysis

4. Evidence
(Quote the exact log evidence)

5. Indicators of Compromise (IoCs)

6. Risk Assessment

7. Recommendations

8. Conclusion

Rules

• Only use evidence present in the retrieved logs.

• Never invent attacks.

• If insufficient evidence exists, clearly mention it.

User Question

{user_question}

Retrieved Logs

{retrieved_logs}
"""

        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error during analysis: {e}"


# For testing directly in VS Code
if __name__ == "__main__":

    question = "Show suspicious activities in the logs"

    result = ask_rag(question)

    print("\n===== AI ANALYSIS =====\n")
    print(result)