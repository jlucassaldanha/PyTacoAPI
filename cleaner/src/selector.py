import pandas as pd
from typing import List

def data_selector(
	df: pd.DataFrame, 
	cols: List[str] = [
        'numero_do_alimento',
		'categoria',
        'descricao_dos_alimentos',
        'energia_kcal',
        'proteina_g',
        'lipideos_g',
        'carboidrato_g',
        'fibra_alimentar_g'
    ]
) -> pd.DataFrame:
	df_final = df[cols].copy()
	
	return df_final