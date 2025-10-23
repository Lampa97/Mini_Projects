from unittest import TestCase
from project_3.models.cpu import CPU


class CPUTest(TestCase):
    def setUp(self):
        self.c1 = CPU('Core i5', 'Intel', 10, 0, 10, 'AMD', 20)

    def test_repr(self):
        self.assertEqual(repr(self.c1), '''CPU(name=Core i5, manufacturer=Intel,
        cores=10, socket=AMD, power watts=20)''')

    def test_str(self):
        self.assertEqual(str(self.c1), 'Core i5')

    def test_claim(self):
        self.c1.claim(2)
        self.assertEqual(self.c1.total, 8)
        self.assertEqual(self.c1.allocated, 2)

    def test_freeup(self):
        self.c1.claim(5)
        self.c1.freeup(2)
        self.assertEqual(self.c1.total, 7)
        self.assertEqual(self.c1.allocated, 3)

    def test_died(self):
        self.c1.claim(2)
        self.c1.died(2)
        self.assertEqual(self.c1.total, 6)
        self.assertEqual(self.c1.allocated, 2)

    def test_purchased(self):
        self.c1.purchased(5)
        self.assertEqual(self.c1.total, 15)

    def test_wrong_init(self):
        with self.assertRaises(AttributeError):
            CPU(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(ValueError):
            CPU('Nice', 'Company', -5, 0, 0, 0, 0)

        with self.assertRaises(ValueError):
            CPU('Nice', 'Company', 6, -2, 0, 0, 0)

        with self.assertRaises(ValueError):
            CPU('Nice', 'Company', 6, 2, 0, 0, 0)

        with self.assertRaises(AttributeError):
            CPU('Nice', 'Company', 6, 2, 4, 0, 3)

        with self.assertRaises(ValueError):
            CPU('Nice', 'Company', 6, 2, 4, 'Extra', 0)

    def test_correct_init(self):
        r2 = CPU('CORe i7', 'INTel', '5', '2', '6', 'Mega', '20')
        self.assertEqual(r2.name, 'Core i7')
        self.assertEqual(r2.manufacturer, 'Intel')
        self.assertEqual(r2.total, 5)
        self.assertEqual(r2.allocated, 2)
        self.assertEqual(r2.cores, 6)
        self.assertEqual(r2.socket, 'MEGA')
        self.assertEqual(r2.power_watts, 20)
        self.assertEqual(r2.category, 'cpu')

    def test_wrong_types_for_calculation(self):
        with self.assertRaises(TypeError):
            self.c1.claim('Mouse')

        with self.assertRaises(TypeError):
            self.c1.freeup('Mouse')

        with self.assertRaises(TypeError):
            self.c1.died('Mouse')

        with self.assertRaises(TypeError):
            self.c1.purchased('Mouse')

    def test_excessive_amount_calculations(self):
        with self.assertRaises(ValueError):
            self.c1.claim(11)

        with self.assertRaises(ValueError):
            self.c1.freeup(11)

        with self.assertRaises(ValueError):
            self.c1.died(11)

    def test_negative_amount_calculations(self):
        with self.assertRaises(ValueError):
            self.c1.claim(-11)

        with self.assertRaises(ValueError):
            self.c1.freeup(-11)

        with self.assertRaises(ValueError):
            self.c1.died(-11)

        with self.assertRaises(ValueError):
            self.c1.purchased(-11)
