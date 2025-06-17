import json

class FileHandler:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.read_data_from_file()
        self.index = 0

    def read_data_from_file(self):
        with open(self.file) as file:
            return json.load(file)

    def write_data_to_file(self, new_data):
        self.data.append(new_data)
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data, indent=4))

    def lookup_for_country_in_data(self, country_name):
        for country in self.data:
            if country.get("full_name").lower() == country_name.lower():
                return country

    def __getitem__(self, item):
        for country in self.data:
            if country.get("full_name").lower() == item.lower():
                return country

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration