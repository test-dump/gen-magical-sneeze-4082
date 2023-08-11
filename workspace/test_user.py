import pytest
from user import User

def test_user_creation():
    user = User('johndoe', 'password123', 'owner')
    assert user.username == 'johndoe'
    assert user.validate_password('password123')
    assert user.role == 'owner'
