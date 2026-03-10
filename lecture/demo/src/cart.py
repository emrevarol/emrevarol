def calc(items, user, d=False):
    t = 0

    for i in items:
        if i["type"] == "book":
            t += i["price"] * 0.9
        else:
            t += i["price"]

    if d:
        t = t - t * 0.1

    if user is not None:
        if "is_premium" in user:
            if user["is_premium"] == True:
                t = t - t * 0.05

    return t


def process_cart(items, user):
    total = calc(items, user, True)
    print("cart processed")
    return total
