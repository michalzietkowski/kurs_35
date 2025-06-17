user_dict = {
        "name": "Piotr Wiśniewski",
        "age": 40,
        "email": "email.com",
        "address": "Wrocław, Polska",
        "zip_code": "50-001",
        "city": "Wrocław",
        "country": "Polska",
        "oceny": {
            "math": 5,
            "english": 4,
            "history": 3
        }
    }



class Users:
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f"Users({self.user})"

    def __int__(self):
        return len(self.user)

    def __getitem__(self, item):
        return self.user.get(item, "Item not found")

    def __setitem__(self, key, value):
        print(key)
        key_1, key_2 = key
        print(key_1)
        print(key_2)
        self.user[key] = value


user = Users(user_dict)
print(user.user.get("name"))

print(user.user.get("email"))

print(user["name"])
print(user["email"])
print(user["address"])
print(user["zip_code_2"])

print(user["zip_code_2"])
print(user["oceny"]["math"])
user["oceny", "wf"] = 5
print(user["oceny", "wf"])