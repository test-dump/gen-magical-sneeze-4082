import pytest
from product import Product

def test_product_creation():
    product = Product('Shirt', 'S', 'Blue', cost=20)
    assert product.name == 'Shirt'
    assert product.size == 'S'
    assert product.color == 'Blue'
    assert product.cost == 20

def test_update_product_attributes():
    product = Product('Shirt', 'S', 'Blue', cost=20)
    product.update('Shirt', 'M', 'Red', 25)
    assert product.size == 'M'
    assert product.color == 'Red'
    assert product.cost == 25
