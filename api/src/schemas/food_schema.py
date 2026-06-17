from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import Any

class FoodResponse(BaseModel):
	id: int
	description: str
	energy_kcal: float | None = None
	protein_grams: float | None = None
	fat_grams: float | None = None
	carbohydrate_grams: float | None = None
	fiber_grams: float | None = None

	model_config = ConfigDict(
		alias_generator=to_camel,
		populate_by_name=True
	) 

class FoodListResponse(BaseModel):
	data: list[Any]

	model_config = ConfigDict(
		alias_generator=to_camel,
		populate_by_name=True
	) 

