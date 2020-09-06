from functools import reduce


def join(a: str, b: str) -> str:
    return a + " " + b


result = reduce(join, ["I", "Love", "Python", "so", "much"])
print(result)
