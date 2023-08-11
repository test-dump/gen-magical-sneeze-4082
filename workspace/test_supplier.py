import pytest
from supplier import Supplier

def test_supplier_creation():
    supplier = Supplier('John Doe', 'john@example.com', '1234567890')
    assert supplier.name == 'John Doe'
    assert supplier.email == 'john@example.com'
    assert supplier.phone == '1234567890
