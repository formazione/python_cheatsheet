from functools import partial


def full_price(price: float, vat: int) -> float:
    "Returns price + vat"
    return price * (100 + vat) / 100


price22 = partial(full_price, vat=22)
price10 = partial(full_price, vat=10)

print(price22(1500))
print(full_price(1500, 22))
print(price10(1500))
print(full_price(1500, 10))
