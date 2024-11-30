
from poems import POEM_ONE, POEM_TWO
from sign import SIGN_TEMPLATE

author_name = "Іван Петренко"

sign_message = SIGN_TEMPLATE.format(author_name)
print(sign_message)

wishes = "Більше практичних завдань\nЗрозумілі пояснення"
print(wishes)

separator = "*" * 74
print(separator)

print(POEM_ONE)
print(separator)

print(POEM_TWO)
print(separator)
