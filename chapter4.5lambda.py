divide = lambda x, y: None if y == 0 else x / y


def divider(x,y):
    """This is a lambda function for dividing. """
    return x / y if y != 0 else None # type: ignore

print(divider(5, 1))
    