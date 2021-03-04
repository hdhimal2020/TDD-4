import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


testString = 'calculator'


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# Group project - Part 2: TDD

# Test # 1 - calculate 5 notebooks price  = $37.5 total
def test_CanCalculateFiveNotebooksPrice(invoice, products):
    invoice.fiveNotebooks(products)
    assert invoice.fiveNotebooks(products) == 37.5


# Test # 2 - calculate a 7.25% tax + the pure price
def test_CanCalculateTax(invoice, products):
    invoice.totalTax(products)
    assert invoice.totalTax(products) == 74.41

