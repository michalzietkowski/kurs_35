def add_numbers(number1, number2):
    return number1 + number2


def format_user_profile(user):
    """
    Zwraca sformatowany profil użytkownika na podstawie słownika z danymi.
    """
    full_name = f"{user['first_name']} {user['last_name']}"
    age = user.get("age", "unknown")
    email = user.get("email", "no email provided")
    is_admin = "Yes" if user.get("is_admin", False) else "No"

    return {
        "full_name": full_name,
        "age": age,
        "email": email,
        "admin": is_admin
    }
