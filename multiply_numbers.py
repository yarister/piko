
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(2, 3, 4))  # Вывод: 24
print(multiply(5, 6))     # Вывод: 30
