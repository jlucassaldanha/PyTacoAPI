from fastapi import APIRouter
from api.src.schemas.food_schema import FoodListResponse
from api.src.schemas.category_schema import CategoryListResponse
from api.src.repository.json_store import TacoJsonRepository

router = APIRouter(prefix="/taco", tags=["Taco"])

@router.get("/category", response_model=CategoryListResponse)
def list_category():
	all_data = TacoJsonRepository.get_all_data()

	category_list = []
	for category in all_data:
		category_list.append(category.get("category"))

	return {
		"data": category_list 
	}

@router.get("/{category}/food", response_model=FoodListResponse)
def list_food_by_category(category: str):
	all_data = TacoJsonRepository.get_all_data()
	
	food_list = []
	for food_category in all_data:
		category_name = food_category.get("category")
		if category_name == category:
			food_list = food_category.get("foods")

	return {
		"data": food_list 
	}
