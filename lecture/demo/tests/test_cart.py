from src.cart import calc


def test_calc():
    items = [{"type": "book", "price": 100}]
    user = {"is_premium": True}
    assert calc(items, user, True) > 0
