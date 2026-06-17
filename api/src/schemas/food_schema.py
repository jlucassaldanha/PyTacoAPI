from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class FoodResponse(BaseModel):
	id: int
	category: str
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