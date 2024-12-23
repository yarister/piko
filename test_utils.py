def get_list_of_strings(items: list) ->list[str]:
    result = []
    for item in items:
        if type(item) == str:
            result.append(item)
    return result