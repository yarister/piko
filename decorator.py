
def check_integer_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result + 10
        return result
    return wrapper
