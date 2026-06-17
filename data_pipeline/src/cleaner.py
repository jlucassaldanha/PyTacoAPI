import pandas as pd
import numpy as np
from typing import List
from src.config import TACO_COLUMN_MAP

def normalize_taco_markers(df: pd.DataFrame) -> pd.DataFrame:
    df_cleaned = df.copy()
    df_cleaned = df_cleaned.replace({'Tr': 0, 'NA': None, '*': None})
    return df_cleaned

def extract_categories(df: pd.DataFrame) -> pd.DataFrame:
	df_cleaned = df.copy()

	numeric_ids = pd.to_numeric(df_cleaned['id'], errors='coerce')

	is_category = (
		numeric_ids.isna() &
		df_cleaned['id'].notna() &
		~df_cleaned['id'].str.contains('Número do', case=False, na=False) &
		~df_cleaned['id'].str.contains('Alimento', case=False, na=False)
	)

	df_cleaned['category'] = np.where(is_category, df_cleaned['id'], np.nan)

	df_cleaned['category'] = df_cleaned['category'].ffill()

	return df_cleaned

def remove_structural_garbage(df: pd.DataFrame) -> pd.DataFrame:
	df_cleaned = df.copy()
	first_column = df_cleaned.columns[0]
	df_cleaned[first_column] = pd.to_numeric(df_cleaned[first_column], errors='coerce')
	df_cleaned = df_cleaned.dropna(subset=[first_column])
	return df_cleaned

def apply_column_names(df: pd.DataFrame, col_map: dict) -> pd.DataFrame:
    df_cleaned = df.copy()
    df_cleaned = df_cleaned.rename(columns=col_map)
    return df_cleaned

def convert_types(df: pd.DataFrame, numeric_columns: list) -> pd.DataFrame:
	df_cleaned = df.copy()
	for col in numeric_columns:
		if col in df_cleaned.columns:
			df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")
	return df_cleaned

def data_selector(
	df: pd.DataFrame, 
	cols: List[str]
) -> pd.DataFrame:
	df_final = df[cols].copy()
	
	return df_final

def clean_taco_data(df_raw: pd.DataFrame) -> pd.DataFrame:
	df = apply_column_names(df_raw, TACO_COLUMN_MAP)
	df = extract_categories(df)
	df = normalize_taco_markers(df)
	df = remove_structural_garbage(df)
	cols_to_numeric = [
        'energyKcal', 'proteinGrams', 'fatGrams', 
        'carbohydrateGrams', 'fiberGrams'
    ]
	df = convert_types(df, cols_to_numeric)
	df['id'] = df['id'].astype(int)
	df = df.reset_index(drop=True)
	selected_cols = [
        'id',
		'category',
        'description',
        'energyKcal',
        'proteinGrams',
        'fatGrams',
        'carbohydrateGrams',
        'fiberGrams'
    ]
	df = data_selector(df, selected_cols)
	
	return df
