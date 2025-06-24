'''
**Zadanie: Transformacja Macierzy**
Napisz program, który przetworzy plik CSV zawierający tablicę liczb i zastosuje serię transformacji określonych przez użytkownika. Program powinien odczytać plik wejściowy, zastosować zadane transformacje, a następnie zapisać go do wskazanego pliku wyjściowego.
Uruchomienie programu przez terminal:
python matrix_transform.py <plik_wejsciowy> <plik_wyjsciowy> <transformacja_1> <transformacja_2> ... <transformacja_n>
- <plik_wejsciowy> - nazwa pliku, z którego odczytane zostaną dane, np. data.csv
- <plik_wyjsciowy> - nazwa pliku, do którego zostanie zapisany wynik, np. result.csv
- <transformacja_x> - Transformacja w postaci "operacja, parametry" - operacja może być np. 'add', 'mult', 'div', a parametry będą określały wartości do zastosowania transformacji (np. dla 'add' będą to wartości dodane do każdej komórki w danej kolumnie lub wierszu).
Operacje transformacji:
- add,row,index,value - Dodaj wartość do każdego elementu w wierszu o zadanym indeksie.
- add,col,index,value - Dodaj wartość do każdego elementu w kolumnie o zadanym indeksie.
- mult,row,index,value - Pomnóż każdy element w wierszu przez wartość.
- mult,col,index,value - Pomnóż każdy element w kolumnie przez wartość.

[
    1, 2, 3
    4, 5, 6
    7, 8, 9
]

add, row,0,10

[
    11, 12, 13
    4, 5, 6
    7, 8, 9
]

mult, col,1,5

[
    11, 60, 13
    4, 10, 6
    7, 15, 9
]
'''
import sys
from file_handler import CsvFileHandler, JsonFileHandler, TxtFileHandler, PickleFileHandler

arguments = sys.argv[1:]
print(arguments)

#
# temp_matrix =  [[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]]
#
# value_1 = temp_matrix[0][0]

input_file = arguments[0]
output_file = arguments[1]

if input_file.endswith('.csv'):
    input_file_handler = CsvFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
elif input_file.endswith('.json'):
    input_file_handler = JsonFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
elif input_file.endswith('.txt'):
    input_file_handler = TxtFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
elif input_file.endswith('pkl'):
    input_file_handler = PickleFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
else:
    raise ValueError("Unsupported file type. Please use .csv, .json, or .txt files.")

if output_file.endswith('.csv'):
    output_file_handler = CsvFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
elif output_file.endswith('.json'):
    output_file_handler = JsonFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
elif output_file.endswith('.txt'):
    output_file_handler = TxtFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
elif output_file.endswith('.pkl'):
    output_file_handler = PickleFileHandler(input_file_path=input_file, output_file_path=output_file, transformations=arguments[2:])
else:
    raise ValueError("Unsupported output file type. Please use .csv, .json, or .txt files.")

input_file_handler.data = input_file_handler.load_data()
input_file_handler.do_transformations()
output_file_handler.data = input_file_handler.data
output_file_handler.save_data()