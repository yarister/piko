
from decorator import check_integer_result

@check_integer_result
def my_function(x, y):
    return x + y

@check_integer_result
def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(my_function(5, 5))  # 20
    print(my_function(3, 2))  # 15
    print(divide(10, 2))  # 15
    print(divide(7, 2))  # 3.5
