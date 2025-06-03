from zajecia_12.math_module import add_numbers, format_user_profile
import pytest

@pytest.fixture
def sample_user():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "age": 20,
        "email": "johndoe@gmail.com",
        "is_admin": True
    }

@pytest.fixture
def expected_user_profile():
    return {
        "full_name": "John Doe",
        "age": 20,
        "email": "johndoe@gmail.com",
        "admin": "Yes"
    }


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add_numbers_parametrized(num1, num2, expected):
    assert add_numbers(num1, num2) == expected


def test_add_numbers_throws_exception():
    with pytest.raises(TypeError):
        add_numbers("a", 1)

def test_format_user_profile(sample_user, expected_user_profile):
    assert format_user_profile(sample_user) == expected_user_profile


def test_format_user_profile_proper_full_name(sample_user, expected_user_profile):
    user_profile = format_user_profile(sample_user)
    assert user_profile["full_name"] == "John Doe"
