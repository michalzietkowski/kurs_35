import csv
import json
import pickle
from abc import ABC, abstractmethod



class FileHandler(ABC):
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.data = None
        self.transformations = transformations

    @abstractmethod
    def load_data(self):
        """Load data from the input file."""
        pass

    @abstractmethod
    def save_data(self):
        """Save data to the output file."""
        pass


    def do_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            operation = transformation_list[0]
            axis = transformation_list[1]
            index = int(transformation_list[2])
            value = int(transformation_list[3])
            if operation == "add":
                if axis == "row":
                    self.add_row(index, value)
                elif axis == "col":
                    self.add_col(index, value)
            elif operation == "mult":
                if axis == "row":
                    self.mult_row(index, value)
                elif axis == "col":
                    self.mult_col(index, value)

    def add_row(self, index, value):
        for position, item in enumerate(self.data[index]):
            self.data[index][position] += value

    def add_col(self, index, value):
        for row in self.data:
            row[index] += value

    def mult_row(self, index, value):
        for position, item in enumerate(self.data[index]):
            self.data[index][position] *= value

    def mult_col(self, index, value):
        for row in self.data:
            row[index] *= value


class CsvFileHandler(FileHandler):
    def load_data(self):
        """Load data from a CSV file."""
        with open(self.input_file) as file:
            reader = csv.reader(file)
            temp_matrix = []
            for row in reader:
                temp_row = []
                for number in row:
                    temp_row.append(int(number))
                temp_matrix.append(temp_row)
        return temp_matrix

    def save_data(self):
        with open (self.output_file, 'w+') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)


class JsonFileHandler(FileHandler):
    def load_data(self):
        """Load data from a JSON file."""
        with open(self.input_file) as file:
            return json.load(file)

    def save_data(self):
        with open(self.output_file, 'w+') as file:
            file.write(json.dumps(self.data, indent=4))

class TxtFileHandler(FileHandler):
    def load_data(self):
        pass

    def save_data(self):
        pass


class PickleFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'rb') as file:
            return pickle.load(file)

    def save_data(self):
        with open(self.output_file, 'wb') as file:
            file.write(pickle.dumps(self.data))
