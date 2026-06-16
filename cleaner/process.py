from src.config import RAW_DATA_PATH, TARGET_SHEET, PROCESSED_DATA_PATH
from src.reader import load_raw_taco
from src.cleaner import clean_taco_data
from src.selector import data_selector
from src.json_parser import create_json

def main() -> None:
	print("Iniciando...")

	try:
		df_raw = load_raw_taco(RAW_DATA_PATH, sheet_id=TARGET_SHEET, skip_rows=3)
		print(f"Dados carregados! Linhas: {df_raw.shape[0]}, Colunas: {df_raw.shape[1]}")

		print("Iniciando pipeline de limpeza...")
		df_cleaned = clean_taco_data(df_raw)
		print("Limpeza concluída.")

		df_final = data_selector(df_cleaned)

		print(df_final)

		create_json(df_final, PROCESSED_DATA_PATH)
		df_final.to_excel("inspecao_visual.xlsx", index=False)

	except FileNotFoundError as e:
		print(e)


if __name__ == "__main__":
	main()