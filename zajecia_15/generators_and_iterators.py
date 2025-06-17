
# users = [{
#         "name": "Jan Kowalski",
#         "age": 30,
#         "email": "jan.kowalski@gmail.com",
#         "address": "Warszawa, Polska",
#         "zip_code": "00-001",
#         "city": "Warszawa",
#         "country": "Polska",
#     },
#     {
#         "name": "Anna Nowak",
#         "age": 25,
#         "email": "anna.nowak@gmail.com",
#         "address": "Kraków, Polska",
#         "zip_code": "31-001",
#         "city": "Kraków",
#         "country": "Polska",
#     },
#     {
#         "name": "Piotr Wiśniewski",
#         "age": 40,
#         "email": "email.com",
#         "address": "Wrocław, Polska",
#         "zip_code": "50-001",
#         "city": "Wrocław",
#         "country": "Polska",
#     }
# ]
#
# def address_parser_for_users(users):
#     parsed_users = []
#     for user in users:
#         parsed_users.append({
#             "name": user.get("name"),
#             "age": user.get("age"),
#             "email": user.get("email"),
#             "full_address": user.get("address") + ", " + user.get("zip_code") + " " + user.get("city") + ", " + user.get("country")
#         })
#     return parsed_users
# #
# users_in_our_system = address_parser_for_users(users)
# print(type(users_in_our_system))
# print(users_in_our_system)
#
#
# def address_parser_for_users_generator(users):
#     for user in users:
#         yield {
#             "name": user.get("name"),
#             "age": user.get("age"),
#             "email": user.get("email"),
#             "full_address": user.get("address") + ", " + user.get("zip_code") + " " + user.get("city") + ", " + user.get("country")
#         }
#
#
# generator = address_parser_for_users_generator(users)
from typing import Iterable, Iterator, Generator

# print(generator)
# for user in range(10):
#     print(next(generator))


# lista_uczniow = ["Jan", "Anna", "Piotr", "Kasia", "Tomek", "Ola", "Marek", "Zosia", "Krzysztof", "Ewa"]
#
# print(type(lista_uczniow))
# print(isinstance(lista_uczniow, Iterable))
# print(isinstance(lista_uczniow, Iterator))
#
#
# lista_iterator = iter(lista_uczniow)
# print(type(lista_iterator))
# print(isinstance(lista_iterator, Iterator))
#
#
# class MyIterator:
#     def __init__(self, data: dict):
#         self.data = data
#         self.iterator = iter(self.data.items())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.iterator)
#
# my_iterator = MyIterator({"a": 1, "b": 2, "c": 3})
#
# print(f"Czy jesteśmy iteratorem? {isinstance(my_iterator, Iterator)}")
# #
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


# class MyIteratorVersion2:
#     def __init__(self, data: dict):
#         self.data = list(data.items())
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index += 1
#             return result
#
#
#
# iterator_v2 = MyIteratorVersion2({"a": 1, "b": 2, "c": 3})
#
# print(iterator_v2.data)
#
# print(next(iterator_v2))
# print(next(iterator_v2))
# print(next(iterator_v2))
# print(next(iterator_v2))


# class MyIterator:
#     def __init__(self, data: dict):
#         self.data = data
#         self.iterator = iter(self.data.items())
#
#     def __iter__(self):
#         return iter(self.data.items())
#
#     # def __next__(self):
#     #     return next(self.iterator)
#
# iterator = MyIterator({'a': 1, 'b': 2, 'c': 3, 'd': 4})
#
# for item in iterator:
#     print(item)
#
# print(isinstance(iterator, Iterator))