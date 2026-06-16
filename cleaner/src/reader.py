import pandas as pd
from pathlib import Path
from typing import Union

def load_raw_taco(file_path: Path, sheet_id: Union[str, int] = 0, skip_rows = 0) -> pd.DataFrame:
	if not file_path.exists():
		raise FileNotFoundError(f"Arquivo não encontrado em: {file_path}")
	
	return pd.read_excel(file_path, sheet_name=sheet_id, skiprows=skip_rows, header=None)