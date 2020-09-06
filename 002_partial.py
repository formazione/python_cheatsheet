from functools import partial


def vat(price, percentage):
    return price * (100 + percentage) / 100


vat22 = partial(vat, percentage=22)
computer_price_plus_vat = vat22(1000)
print(computer_price_plus_vat)
