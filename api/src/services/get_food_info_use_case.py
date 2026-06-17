def get_food_info_use_case(food_list: list[dict[str, str]], food: str) ->  dict[str, str] | None:
	for food_data in food_list:
		description = food_data.get("description")
		if description == food:
			return food_data
	
	return None