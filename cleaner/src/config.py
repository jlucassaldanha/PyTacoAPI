from pathlib import Path
from typing import Union

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "taco_table.xlsx"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "taco_cleaned.json"

TARGET_SHEET: Union[str, int] = 0

TACO_COLUMN_MAP = {
    0: "numero_do_alimento",
    1: "descricao_dos_alimentos",
    2: "umidade_porcento",
    3: "energia_kcal",
    4: "energia_kj",
    5: "proteina_g",
    6: "lipideos_g",
    7: "colesterol_mg",
    8: "carboidrato_g",
    9: "fibra_alimentar_g",
    10: "cinzas_g",
    11: "calcio_mg",
    12: "magnesio_mg",
    # 13 seria o 'Número do Alimento' repetido da pág 2 (vamos ignorar/dropar depois)
    14: "manganes_mg",
    15: "fosforo_mg",
    16: "ferro_mg",
    17: "sodio_mg",
    18: "potassio_mg",
    19: "cobre_mg",
    20: "zinco_mg",
    21: "retinol_mcg",
    22: "re_mcg",
    23: "rae_mcg"
}