def get_food_list_use_case(data: list[dict[str, list[dict[str, str]]]], category: str) ->  list[dict[str, str]]:
	for food_category in data:
		category_name = food_category.get("category")
		if category_name == category:
			return food_category.get("foods")
		
	return []
