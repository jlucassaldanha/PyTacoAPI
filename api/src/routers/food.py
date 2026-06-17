from fastapi import APIRouter
from api.src.schemas.food_schema import FoodResponse
from api.src.repository.json_store import TacoJsonRepository

router = APIRouter(prefix="/food", tags=["Food"])

@router.get("", response_model=list[FoodResponse])
def list_food():
	return TacoJsonRepository.get_all_data()