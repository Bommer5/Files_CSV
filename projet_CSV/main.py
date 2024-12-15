import csv
import variable

class file_CSV :
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        self.reader = csv.reader(self.file)
        try:
            self.header = next(self.reader)
        except StopIteration:
            self.header = None

    def close(self):
        self.file.close()




test = file_CSV(variable.CSV_DIRECTORY)
for i in test.reader:
    print(i)
test.close()

