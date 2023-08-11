import pytest
from salesdata import SalesData
from product import Product

def test_add_sale():
    product = Product('Shirt', 'M', 'Red', cost=25)
    sales_data = SalesData()
    sales_data.add_sale(product, 5)
    assert sales_data.sales[product] == 5

def test_generate_report():
    product = Product('Shirt', 'M', 'Red', cost=25)
    sales_data = SalesData()
    sales_data.add_sale(product, 5)
    report = sales_data.generate_report()
    assert report[product] == 5
