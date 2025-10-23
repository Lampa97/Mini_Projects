class Resource:

    def __init__(self, name: str, manufacturer: str, total: int, allocated: int):
        self.__name = name.capitalize()
        self.__manufacturer = manufacturer.capitalize()
        self.__total = int(total)
        self.__allocated = int(allocated)
        if self.total < 0 or self.allocated < 0:
            raise ValueError('Total and allocated should be 0 or more')

    @property
    def total(self):
        return self.__total

    @property
    def allocated(self):
        return self.__allocated

    @property
    def name(self):
        return self.__name

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def category(self):
        return self.__class__.__name__.lower()

    def __validate_value(self, value, class_):
        if isinstance(value, class_):
            return
        else:
            raise TypeError(f'Wrong type provided. Please provide {class_} type')

    def __validate_positive_int(self, n):
        if n <= 0:
            raise ValueError("Please provide positive number")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, manufacturer={self.manufacturer})'

    def claim(self, n: int):
        """Method to take n resources from the pool (as long as inventory is available)"""
        self.__validate_value(n, int)
        self.__validate_positive_int(n)
        if n > self.total:
            raise ValueError(f'Not enough items in the inventory. You tried to claim - {n} items.'
                             f'\nCurrently in stock - {self.total}')
        self.__total -= n
        self.__allocated += n

    def freeup(self, n: int):
        """Method to return n resources to the pool (e.g. disassembled some builds)"""
        self.__validate_value(n, int)
        self.__validate_positive_int(n)
        if n > self.allocated:
            raise ValueError(f'Less items are allocated. You tried to freeup - {n} items.'
                             f'\nCurrently allocated - {self.allocated}')
        self.__total += n
        self.__allocated -= n

    def died(self, n: int):
        """Method to return and permanently remove inventory from the pool
        (e.g. they broke something) - as long as total available allows it"""
        self.__validate_value(n, int)
        self.__validate_positive_int(n)
        if n > self.total:
            raise ValueError(f'Not enough items in the inventory. You tried to remove - {n} items.'
                             f'\nCurrently in stock - {self.total}')
        self.__total -= n

    def purchased(self, n: int):
        """Method to add inventory to the pool (e.g. they purchased a new CPU)"""
        self.__validate_value(n, int)
        self.__validate_positive_int(n)
        self.__total += n
