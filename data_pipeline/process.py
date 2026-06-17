from src.config import RAW_DATA_PATH, TARGET_SHEET, PROCESSED_DATA_PATH
from src.reader import load_raw_taco
from src.cleaner import clean_taco_data
from src.json_parser import create_json_data, create_json_file

def main() -> None:
	print("Starting...")

	try:
		df_raw = load_raw_taco(RAW_DATA_PATH, sheet_id=TARGET_SHEET, skip_rows=3)
		print("Data loaded!")

		print("Starting cleaner pipeline...")
		df_cleaned = clean_taco_data(df_raw)

		print(df_cleaned)

		print("Creating .json")
		final_data = create_json_data(df_cleaned)
		create_json_file(final_data, PROCESSED_DATA_PATH)
		#df_cleaned.to_excel("inspecao_visual.xlsx", index=False)

	except FileNotFoundError as e:
		print(e)


if __name__ == "__main__":
	main()