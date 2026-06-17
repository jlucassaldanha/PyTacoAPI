from fastapi import APIRouter, HTTPException
from api.src.schemas.food_schema import FoodListResponse, FoodResponse
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

@router.get("/{category}", response_model=FoodListResponse)
def list_food_by_category(category: str):
	all_data = TacoJsonRepository.get_all_data()
	
	food_list = []
	for food_category in all_data:
		category_name = food_category.get("category")
		if category_name == category:
			food_list = food_category.get("foods")
			break
	
	if len(food_list) <= 0:
		raise HTTPException(status_code=404, detail="Category not found")

	return {
		"data": food_list 
	}

@router.get("/{category}/{food}", response_model=FoodResponse)
def get_food_information(category: str, food: str):
	all_data = TacoJsonRepository.get_all_data()
	
	food_list = []
	for food_category in all_data:
		category_name = food_category.get("category")
		if category_name == category:
			food_list = food_category.get("foods")
			break
		
	if len(food_list) <= 0:
		raise HTTPException(status_code=404, detail="Category not found")

	food_info = None
	for food_data in food_list:
		description = food_data.get("description")
		if description == food:
			food_info = food_data
			break

	if not food_info:
		raise HTTPException(status_code=404, detail="Food not found")

	return {
		"data": food_info
	}