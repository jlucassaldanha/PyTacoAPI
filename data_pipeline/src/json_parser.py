import pandas as pd
from pathlib import Path

def create_json(df: pd.DataFrame, file_path: Path) -> pd.DataFrame:
	df.to_json(file_path, orient="records", force_ascii=False, indent=4)