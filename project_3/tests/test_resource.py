from unittest import TestCase
from project_3.models.resource import Resource


class ResourceTest(TestCase):
    def setUp(self):
        self.r1 = Resource('GPU', 'Nvidia', 10, 0)

    def test_repr(self):
        self.assertEqual(repr(self.r1), 'Resource(name=Gpu, manufacturer=Nvidia)')

    def test_str(self):
        self.assertEqual(str(self.r1), 'Gpu')

    def test_claim(self):
        self.r1.claim(2)
        self.assertEqual(self.r1.total, 8)
        self.assertEqual(self.r1.allocated, 2)

    def test_freeup(self):
        self.r1.claim(5)
        self.r1.freeup(2)
        self.assertEqual(self.r1.total, 7)
        self.assertEqual(self.r1.allocated, 3)

    def test_died(self):
        self.r1.claim(2)
        self.r1.died(2)
        self.assertEqual(self.r1.total, 6)
        self.assertEqual(self.r1.allocated, 2)

    def test_purchased(self):
        self.r1.purchased(5)
        self.assertEqual(self.r1.total, 15)

    def test_wrong_init(self):
        with self.assertRaises(AttributeError):
            Resource(1, 2, 3, 4)

        with self.assertRaises(ValueError):
            Resource('Nice', 'Company', -5, 0)

        with self.assertRaises(ValueError):
            Resource('Nice', 'Company', 6, -2)

    def test_correct_init(self):
        r2 = Resource('gpu', 'miCroSoft', '5', '2')
        self.assertEqual(r2.name, 'Gpu')
        self.assertEqual(r2.manufacturer, 'Microsoft')
        self.assertEqual(r2.total, 5)
        self.assertEqual(r2.allocated, 2)
        self.assertEqual(r2.category, 'resource')

    def test_wrong_types_for_calculation(self):
        with self.assertRaises(TypeError):
            self.r1.claim('Mouse')

        with self.assertRaises(TypeError):
            self.r1.freeup('Mouse')

        with self.assertRaises(TypeError):
            self.r1.died('Mouse')

        with self.assertRaises(TypeError):
            self.r1.purchased('Mouse')

    def test_excessive_amount_calculations(self):
        with self.assertRaises(ValueError):
            self.r1.claim(11)

        with self.assertRaises(ValueError):
            self.r1.freeup(11)

        with self.assertRaises(ValueError):
            self.r1.died(11)

    def test_negative_amount_calculations(self):
        with self.assertRaises(ValueError):
            self.r1.claim(-11)

        with self.assertRaises(ValueError):
            self.r1.freeup(-11)

        with self.assertRaises(ValueError):
            self.r1.died(-11)

        with self.assertRaises(ValueError):
            self.r1.purchased(-11)
