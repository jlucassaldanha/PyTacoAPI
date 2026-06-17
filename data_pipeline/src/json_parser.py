import pandas as pd
import numpy as np
from pathlib import Path
import json

def create_json_data(df: pd.DataFrame) -> list:
	df_final = df.replace({np.nan: None})
	final_data = []

	for category, df_group in df_final.groupby('category'):
		food_list = df_group.drop(columns=['category']).to_dict(orient='records')

		final_data.append({
			"category": category,
			"foods": food_list
		})

	return final_data

def create_json_file(data: list, file_path: Path):
	with open(file_path, "w", encoding="utf-8") as file:
		json.dump(data, file, ensure_ascii=False, indent=4)