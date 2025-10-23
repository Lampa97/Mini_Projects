from unittest import TestCase
from project_3.models.storage import HDD, SSD


class StorageTest(TestCase):
    def setUp(self):
        self.hdd = HDD('Hard Drive', 'Intel', 10, 0, 128, 2.5, 7000)
        self.ssd = SSD('Solid Drive', 'Intel', 10, 0, 128, 'PCIe NVMe 3.0 x4')

    def test_repr(self):
        self.assertEqual(repr(self.hdd), '''HDD(name=Hard drive, manufacturer=Intel,
        capacity_GB=128, size=2.5", rpm=7000)''')

        self.assertEqual(repr(self.ssd), '''SSD(name=Solid drive, manufacturer=Intel,
        capacity_GB=128, interface=Pcie nvme 3.0 x4)''')

    def test_str(self):
        self.assertEqual(str(self.hdd), 'Hard drive')
        self.assertEqual(str(self.ssd), 'Solid drive')

    def test_claim(self):
        self.hdd.claim(2)
        self.assertEqual(self.hdd.total, 8)
        self.assertEqual(self.hdd.allocated, 2)

    def test_freeup(self):
        self.hdd.claim(5)
        self.hdd.freeup(2)
        self.assertEqual(self.hdd.total, 7)
        self.assertEqual(self.hdd.allocated, 3)

    def test_died(self):
        self.hdd.claim(2)
        self.hdd.died(2)
        self.assertEqual(self.hdd.total, 6)
        self.assertEqual(self.hdd.allocated, 2)

    def test_purchased(self):
        self.hdd.purchased(5)
        self.assertEqual(self.hdd.total, 15)

    def test_wrong_init(self):
        with self.assertRaises(AttributeError):
            HDD(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(ValueError):
            HDD('Nice', 'Company', -5, 0, 0, 0, 0)

        with self.assertRaises(ValueError):
            HDD('Nice', 'Company', 6, -2, 0, 0, 0)

        with self.assertRaises(ValueError):
            HDD('Nice', 'Company', 6, 2, 0, -5, 2)

        with self.assertRaises(ValueError):
            HDD('Nice', 'Company', 6, 2, 4, 0, -6)

        with self.assertRaises(AttributeError):
            SSD('Nice', 'Company', 6, 2, 4, 100)

    def test_correct_init(self):
        hdd = HDD('HarD', 'INTel', '5', '2', '60', '2.5', '20')
        ssd = SSD('SOLid', 'INTel', '5', '2', '60', 'Mag PCI 4.0')
        self.assertEqual(hdd.name, 'Hard')
        self.assertEqual(hdd.manufacturer, 'Intel')
        self.assertEqual(hdd.total, 5)
        self.assertEqual(hdd.allocated, 2)
        self.assertEqual(hdd.capacity_GB, 60)
        self.assertEqual(hdd.size, 2.5)
        self.assertEqual(hdd.rpm, 20)
        self.assertEqual(hdd.category, 'hdd')

        self.assertEqual(ssd.name, 'Solid')
        self.assertEqual(ssd.manufacturer, 'Intel')
        self.assertEqual(ssd.interface, 'Mag pci 4.0')
        self.assertEqual(ssd.category, 'ssd')

    def test_wrong_types_for_calculation(self):
        with self.assertRaises(TypeError):
            self.hdd.claim('Mouse')

        with self.assertRaises(TypeError):
            self.hdd.freeup('Mouse')

        with self.assertRaises(TypeError):
            self.hdd.died('Mouse')

        with self.assertRaises(TypeError):
            self.hdd.purchased('Mouse')

    def test_excessive_amount_calculations(self):
        with self.assertRaises(ValueError):
            self.hdd.claim(11)

        with self.assertRaises(ValueError):
            self.hdd.freeup(11)

        with self.assertRaises(ValueError):
            self.hdd.died(11)

    def test_negative_amount_calculations(self):
        with self.assertRaises(ValueError):
            self.hdd.claim(-11)

        with self.assertRaises(ValueError):
            self.hdd.freeup(-11)

        with self.assertRaises(ValueError):
            self.hdd.died(-11)

        with self.assertRaises(ValueError):
            self.hdd.purchased(-11)
