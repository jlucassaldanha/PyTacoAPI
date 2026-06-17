from fastapi import APIRouter, HTTPException
from api.src.schemas.food_schema import FoodListResponse, FoodResponse
from api.src.schemas.category_schema import CategoryListResponse
from api.src.repository.json_store import TacoJsonRepository
from api.src.services.get_food_list_use_case import get_food_list_use_case
from api.src.services.get_food_info_use_case import get_food_info_use_case
from api.src.services.get_category_list_use_case import get_category_list_use_case

router = APIRouter(prefix="/taco", tags=["Taco"])

@router.get("/category", response_model=CategoryListResponse)
def list_category():
	all_data = TacoJsonRepository.get_all_data()

	category_list = get_category_list_use_case(all_data)

	return {
		"data": category_list 
	}

@router.get("/{category}", response_model=FoodListResponse)
def list_food_by_category(category: str):
	all_data = TacoJsonRepository.get_all_data()
	
	food_list = get_food_list_use_case(all_data, category)
	
	if len(food_list) <= 0:
		raise HTTPException(status_code=404, detail="Category not found")

	return {
		"data": food_list 
	}

@router.get("/{category}/{food}", response_model=FoodResponse)
def get_food_information(category: str, food: str):
	all_data = TacoJsonRepository.get_all_data()
	
	food_list = get_food_list_use_case(all_data, category)
		
	if len(food_list) <= 0:
		raise HTTPException(status_code=404, detail="Category not found")

	food_info = get_food_info_use_case(food_list, food)

	if not food_info:
		raise HTTPException(status_code=404, detail="Food not found")

	return {
		"data": food_info
	}