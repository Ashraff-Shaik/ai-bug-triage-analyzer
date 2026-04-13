import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
    
    def load_bugs(self) -> pd.DataFrame:
        """Load bug dataset from CSV."""
        if not self.data_path.exists():
            raise FileNotFoundError(f"Bug data not found at {self.data_path}")
        df = pd.read_csv(self.data_path)
        return df
