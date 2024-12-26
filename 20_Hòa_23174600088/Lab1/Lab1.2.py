import json
class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
    def display_data(self):
        if self.data is not None :
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, \Address:{user['address']}")
# Sử dụng lớp JSONReader
path = '20_Hòa_23174600088\Lab1\products.xml'
reader = JSONReader(path)
reader.read_json()
reader.display_data()