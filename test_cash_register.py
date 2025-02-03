import unittest
from decimal import Decimal
from cash_register import item_1_total_cost_right_format, item_2_total_cost_right_format, total_cost_right_format

class TestCashRegister(unittest.TestCase):
    def test_total_cost_format(self):
        self.assertEqual(item_1_total_cost_right_format, Decimal('42.00'))  # Подставь ожидаемое значение
        self.assertEqual(item_2_total_cost_right_format, Decimal('39.11'))  # Подставь ожидаемое значение
        self.assertEqual(total_cost_right_format, Decimal('81.11'))  # Подставь ожидаемое значение

if __name__ == '__main__':
    unittest.main()