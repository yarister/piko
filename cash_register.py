import textwrap
from datetime import datetime
from decimal import Decimal

item_1_title = textwrap.shorten(input('Введіть назву першого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = int(float(input('Введіть бажану кількість першого товару: ')))
item_1_price = Decimal(input('Введіть ціну першого товару: '))

item_2_title = textwrap.shorten(input('Введіть назву другого товару: ').ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = int(float(input('Введіть бажану кількість другого товару: ')))
item_2_price = Decimal(input('Введіть ціну другого товару: '))

item_1_total_cost = item_1_quantity * item_1_price
item_2_total_cost = item_2_quantity * item_2_price

item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('1.00'))
item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('1.00'))

total_cost = item_1_total_cost + item_2_total_cost
total_cost_right_format = total_cost.quantize(Decimal('1.00'))

printing_template = '{}\t\t\t{}\t\t\t{}\t\t\t{}'

print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'Товар\t\t\t\t\t\t\t\t\tКількість\t\tЦіна\t\tВартість')
print(printing_template.format(item_1_title, item_1_quantity, item_1_price, item_1_total_cost_right_format))
print(printing_template.format(item_2_title, item_2_quantity, item_2_price, item_2_total_cost_right_format))
print('~' * 80)
print(printing_template.format('ВСЬОГО'.ljust(20), '-', '-', total_cost_right_format))
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')
