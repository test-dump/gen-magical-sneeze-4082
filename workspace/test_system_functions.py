import pytest
from alert import alert
from autoorder import autoorder
from securelogin import securelogin
from user import User
from product import Product
from inventory import Inventory

def test_alert():
    product = Product('Shirt', 'M', 'Red', 25)
    inventory = Inventory()
    inventory.add_product(product)
    product.stock = 5
    product.reorder_level = 10
    assert alert(inventory) == [product]

def test_autoorder():
    product = Product('Shirt', 'M', 'Red', 25)
    inventory = Inventory()
    inventory.add_product(product)
    product.stock = 5
    product.reorder_level = 10
    assert autoorder(inventory) == [product]

def test_secure_login():
    user = User('johndoe', 'password123', 'owner')
    assert securelogin('johndoe', 'password123') == user
