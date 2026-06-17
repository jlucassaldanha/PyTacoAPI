import json
from pathlib import Path
from typing import Any

class TacoJsonRepository:
	_memory_data: list[dict[str, Any]] = []

	@classmethod
	def load_data(cls, file_path: str) -> None:
		path = Path(file_path).resolve()

		try:
			with open(path, 'r', encoding='utf-8') as file:
				cls._memory_data = json.load(file)
				print(f"{len(cls._memory_data)} alimentos carregados na memória")
		except FileNotFoundError:
			print(f"Arquivo não encontrado: {file_path}")
			cls._memory_data = []

	@classmethod
	def get_all_data(cls) -> list[dict[str, Any]]:
		return cls._memory_data