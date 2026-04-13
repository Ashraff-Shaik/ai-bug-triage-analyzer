import pandas as pd
from pathlib import Path
from .data_loader import DataLoader
from .embedding import EmbeddingGenerator
from .vector_store import VectorStore
from .retriever import BugRetriever
from .llm_engine import LLMEngine

class BugTriageSystem:
    def __init__(self, data_path=None):
        # ✅ Resolve path correctly (works from anywhere)
        if data_path is None:
            BASE_DIR = Path(__file__).resolve().parent.parent
            data_path = BASE_DIR / "data" / "bugs.csv"

        print(f"Using data file: {data_path}")

        self.data_loader = DataLoader(data_path)
        self.embedding_gen = EmbeddingGenerator()
        self.vector_store = VectorStore()
        self.llm = LLMEngine()
        self.bug_df = None
        self.retriever = None
        self._initialize()
    
    def _initialize(self):
        """Load data, build embeddings and index."""
        print("Loading bug dataset...")
        self.bug_df = self.data_loader.load_bugs()
        
        print("Generating embeddings...")
        descriptions = self.bug_df['description'].tolist()
        embeddings = self.embedding_gen.encode(descriptions)
        
        print("Building FAISS index...")
        bug_ids = self.bug_df['bug_id'].tolist()
        self.vector_store.add_embeddings(embeddings, bug_ids)
        
        self.retriever = BugRetriever(self.vector_store, self.bug_df)
        print("Triage system ready!")
    
    def triage(self, bug_description: str):
        """Full triage pipeline."""
        # Embed query
        query_emb = self.embedding_gen.encode([bug_description])[0]
        
        # Retrieve similar bugs
        similar_bugs = self.retriever.retrieve_similar(query_emb, k=3)
        
        # LLM analysis
        analysis = self.llm.analyze_root_cause(bug_description, similar_bugs)
        
        return {
            'similar_bugs': similar_bugs,
            'module': analysis['module'],
            'severity': analysis['severity'],
            'explanation': analysis['explanation'],
            'root_cause': analysis['root_cause'],
            'suggested_fix': analysis['suggested_fix']
        }
