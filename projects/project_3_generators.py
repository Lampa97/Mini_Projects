from collections import namedtuple, defaultdict
from datetime import datetime
import re


class TicketGenerator:

    def __init__(self, filename):
        self.__filename = filename
        self.violations = defaultdict(int)

    def __read_headers(self):
        with open(self.__filename) as f:
            columns = next(f)
            clean_columns = columns.strip('\n').replace(' ', '_').lower().replace(',', ' ')
            return clean_columns

    def __generate_tickets(self):
        clean_columns = self.__read_headers()
        ticket = namedtuple('Ticket', clean_columns)

        with open(self.__filename) as f:
            next(f)
            for line in f:
                data = line.strip('\n').split(',')
                data = [self.convert_data_types(item) for item in data]
                yield ticket(*data)

    def calculate_violations_by_car_make(self):
        self.violations = defaultdict(int)
        tickets = self.__generate_tickets()
        for ticket in tickets:
            car_make = ticket.vehicle_make
            self.violations[car_make] += 1
        return self.violations


    @staticmethod
    def convert_data_types(data_column):
        if data_column.isdigit():
            return int(data_column)
        elif re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', data_column):
            return datetime.strptime(data_column, '%m/%d/%Y').date()
        else:
            return data_column.strip().upper()




ticket_generator = TicketGenerator('nyc_parking_tickets_extract.csv')

violations = ticket_generator.calculate_violations_by_car_make()

print(violations)



