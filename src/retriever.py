from typing import List, Tuple
import numpy as np
import pandas as pd

class BugRetriever:
    def __init__(self, vector_store, bug_df: pd.DataFrame):
        self.vector_store = vector_store
        self.bug_df = bug_df
    
    def retrieve_similar(self, query_embedding, k=3) -> List[dict]:
        """Retrieve top k similar bugs."""
        distances, indices = self.vector_store.search(query_embedding, k)
        similar_bugs = []
        for i, idx in enumerate(indices):
            if idx < len(self.bug_df):
                bug = self.bug_df.iloc[idx].to_dict()
                bug['similarity_score'] = 1 / (1 + distances[i])  # Convert distance to similarity
                similar_bugs.append(bug)
        return similar_bugs
