def f(expr, old_list, test=lambda x: True):
    """
    Applies an expression to elements of a list based on a test condition.

    Parameters:
    expr (function): A function to apply to each element that passes the test.
    old_list (list): The list of elements to process.
    test (function, optional): A function that returns True for elements to process. Defaults to a function that always returns True.

    Returns:
    list: A new list with the processed elements.
    """
    new_list = []
    for e in old_list:
        if test(e):
            new_list.append(expr(e))
    return new_list

result = f(lambda x: x**2, [1,2,3,4,5], lambda x: x%2 == 0)
print(result)