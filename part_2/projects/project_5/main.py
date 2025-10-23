import csv
from collections import namedtuple
from contextlib import contextmanager

f_names = "cars.csv", "personal_info.csv"


class CSVContextManager:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self._f = open(self.filename, self.mode)
        dialect = self.get_dialect()
        self._reader = csv.reader(self._f, dialect)
        headers = map(lambda s: s.lower(), next(self._reader))
        self._nt = namedtuple("Data", headers)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # No specific cleanup needed for CSV files
        self._f.close()
        return False

    def get_dialect(self):
        with open(self.filename) as f:
            sample = f.read(1000)
            f.seek(0)
            return csv.Sniffer().sniff(sample)

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            row = next(self._reader)
            return self._nt(*row)


with CSVContextManager("cars.csv") as reader:
    for _ in range(5):
        print(next(reader))
    print("---\n")


@contextmanager
def csv_context_manager(filename, mode="r"):
    f = open(filename, mode)
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda s: s.lower(), next(reader))
        nt = namedtuple("Data", headers)
        yield (nt(*row) for row in reader)
    finally:
        f.close()


with csv_context_manager("cars.csv") as reader:
    for _ in range(5):
        row = next(reader)
        print(row)
# Just print the first row as a sample

print("hello" "world" * 2)
