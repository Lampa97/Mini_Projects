from project_3.models.resource import Resource


class Storage(Resource):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, capacity_GB: int):
        super().__init__(name, manufacturer, total, allocated)
        self.__capacity_GB = int(capacity_GB)
        if self.capacity_GB < 0:
            raise ValueError('Capacity should be 1 or more GB')

    @property
    def capacity_GB(self):
        return self.__capacity_GB


class HDD(Storage):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
                 capacity_GB: int, size: float, rpm: int):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.__size = float(size)
        self.__rpm = int(rpm)
        if self.size < 0 or self.rpm < 0:
            raise ValueError('Size and rpm should be more than 0')

    @property
    def size(self):
        return self.__size

    @property
    def rpm(self):
        return self.__rpm

    def __repr__(self):
        return f'''{self.__class__.__name__}(name={self.name}, manufacturer={self.manufacturer},
        capacity_GB={self.capacity_GB}, size={self.size}", rpm={self.rpm})'''


class SSD(Storage):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, capacity_GB: int, interface: str):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.__interface = interface.capitalize()

    @property
    def interface(self):
        return self.__interface

    def __repr__(self):
        return f'''{self.__class__.__name__}(name={self.name}, manufacturer={self.manufacturer},
        capacity_GB={self.capacity_GB}, interface={self.interface})'''
