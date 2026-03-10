def calc(items, vip=False):
    total = 0

    for i in items:
        if i["type"] == "book":
            total += i["price"] * 0.9
        elif i["type"] == "electronics":
            total += i["price"]
        else:
            total += i["price"]

    if vip == True:
        total = total - total * 0.05

    return total


def checkout(items, user):
    total = calc(items, user["vip"])
    print("checking out order...")
    print("total is", total)
    return {"ok": True, "total": total}
