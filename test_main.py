# from main import get_weather

# def test_get_weather():
#     assert(get_weather(21) == "cold")

# from main import add, divide
# import pytest

# def test_add():
#     assert add(2, 3) == 5 "2 + 3 should be 5"
#     assert add(-1 , 1) == 5 "2 + 3 should be 5"
#     assert add(2, 3) == 5 "2 + 3 should be 5"
    
# def test_divide():
#     with pytest.raises(ValueError, match= "Cannot divide by zero"):
#         divide(10, 0)

import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "jhon@example.com") == True
    assert user_manager.get_user("john_doe") == "jhon@example.com"