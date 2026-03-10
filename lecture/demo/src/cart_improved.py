BOOK_DISCOUNT_RATE = 0.10
GENERAL_DISCOUNT_RATE = 0.10
PREMIUM_DISCOUNT_RATE = 0.05


def calculate_item_price(item):
    item_type = item["type"]
    price = item["price"]

    if item_type == "book":
        return price * (1 - BOOK_DISCOUNT_RATE)

    return price


def apply_general_discount(total_price, discount_enabled):
    if not discount_enabled:
        return total_price

    return total_price * (1 - GENERAL_DISCOUNT_RATE)


def apply_premium_discount(total_price, user):
    if not user or not user.get("is_premium", False):
        return total_price

    return total_price * (1 - PREMIUM_DISCOUNT_RATE)


def calculate_cart_total(items, user, discount_enabled=False):
    total_price = 0

    for item in items:
        total_price += calculate_item_price(item)

    total_price = apply_general_discount(total_price, discount_enabled)
    total_price = apply_premium_discount(total_price, user)

    return total_price


def process_cart(items, user):
    total_price = calculate_cart_total(items, user, discount_enabled=True)
    return total_price
