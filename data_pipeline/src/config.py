from pathlib import Path
from typing import Union

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "taco_table.xlsx"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "taco_cleaned.json"

TARGET_SHEET: Union[str, int] = 0

TACO_COLUMN_MAP = {
    0: "id",
    1: "description",
    #2: "umidade_porcento",
    3: "energyKcal",
    #4: "energyKj",
    5: "proteinGrams",
    6: "fatGrams",
    #7: "colesterol_mg",
    8: "carbohydrateGrams",
    9: "fiberGrams",
    #10: "cinzas_g",
    #11: "calcio_mg",
    #12: "magnesio_mg",
    #13 seria o 'Número do Alimento' repetido da pág 2 (vamos ignorar/dropar depois)
    #14: "manganes_mg",
    #15: "fosforo_mg",
    #16: "ferro_mg",
    #17: "sodio_mg",
    #18: "potassio_mg",
    #19: "cobre_mg",
    #20: "zinco_mg",
    #21: "retinol_mcg",
    #22: "re_mcg",
    #23: "rae_mcg"
}