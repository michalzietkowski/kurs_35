class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        print("Generating report...")
        print("Retrieving data from users...")
        print("Formatting report content...")
        return f"Report: {self.title}\nContent: {self.content}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate())



class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        print("Generating report...")
        print("Retrieving data from users...")
        print("Formatting report content...")
        return f"Report: {self.title}\nContent: {self.content}"


class Invoice:
    def __init__(self, title, invoice):
        self.title = title
        self.invoice = invoice

    def generate(self):
        print("Generating invoice...")
        print("Retrieving data from users...")
        print("Formatting invoice content...")
        return f"Invoice: {self.title}\nContent: {self.invoice}"


class TaxDocument:
    def __init__(self, title, tax_info):
        self.title = title
        self.tax_info = tax_info

    def generate(self):
        print("Generating tax document...")
        print("Retrieving data from users...")
        print("Formatting tax document content...")
        return f"Tax Document: {self.title}\nContent: {self.tax_info}"


class FileSaver:
    @staticmethod
    def save(filename, content):
        with open(filename, "w") as file:
            file.write(content)
        print(f"Content saved to {filename}")