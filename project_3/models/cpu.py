from project_3.models.resource import Resource


class CPU(Resource):
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
                 cores: int, socket: str, power_watts: int):
        super().__init__(name, manufacturer, total, allocated)
        self.__cores = int(cores)
        self.__power_watts = int(power_watts)
        if self.cores < 1 or self.power_watts < 1:
            raise ValueError('Cores and power_watts should be 1 or more')
        self.__socket = socket.upper()

    @property
    def cores(self):
        return self.__cores

    @property
    def socket(self):
        return self.__socket

    @property
    def power_watts(self):
        return self.__power_watts

    def __repr__(self):
        return f'''{self.__class__.__name__}(name={self.name}, manufacturer={self.manufacturer},
        cores={self.cores}, socket={self.socket}, power watts={self.power_watts})'''
