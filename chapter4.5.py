divide = lambda x, y: None if y == 0 else x / y


def divide(x,y):
    return x / y if y != 0 else None # type: ignore

print(divide(5, 1))
    