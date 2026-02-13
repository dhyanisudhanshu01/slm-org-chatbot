import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

class BitextRAG:
    def __init__(self, csv_path="data/bitext.csv"):
        self.df = pd.read_csv(csv_path)

        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(self.df["instruction"].tolist(), show_progress_bar=True)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.df.iloc[idx]["response"])

        return results