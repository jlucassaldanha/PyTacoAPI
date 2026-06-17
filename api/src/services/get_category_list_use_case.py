def get_category_list_use_case(data: list[dict[str, list[dict[str, str]]]]) -> list:
	category_list = []
	for category in data:
		category_list.append(category.get("category"))
	
	return category_list