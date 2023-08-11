import pytest
from inventory import Inventory
from product import Product

def test_add_product():
    inventory = Inventory()
    product = Product('Shirt', 'S', 'Blue', cost=20)
    inventory.add_product(product)
    assert len(inventory.products) == 1

def test_update_product():
    inventory = Inventory()
    product = Product('Shirt', 'S', 'Blue', cost=20)
    inventory.add_product(product)
    product.update('Shirt', 'M', 'Red', 25)
    assert inventory.products[0].size == 'M'
    assert inventory.products[0].color == 'Red'
    assert inventory.products[0].cost == 25

def test_remove_product():
    inventory = Inventory()
    product = Product('Shirt', 'S', 'Blue', cost=20)
    inventory.add_product(product)
    inventory.remove_product(product)
    assert len(inventory.products) == 0
