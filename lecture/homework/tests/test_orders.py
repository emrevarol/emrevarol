from src.orders import calc


def test_calc():
    items = [{"type": "book", "price": 100}]
    assert calc(items, False) > 0
