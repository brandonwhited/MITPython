# def f(expr, old_list, test=lambda x: True):
#     """
#     Applies an expression to elements of a list based on a test condition.

#     Parameters:
#     expr (function): A function to apply to each element that passes the test.
#     old_list (list): The list of elements to process.
#     test (function, optional): A function that returns True for elements to process. Defaults to a function that always returns True.

#     Returns:
#     list: A new list with the processed elements.
#     """
#     new_list = []
#     for e in old_list:
#         if test(e):
#             new_list.append(expr(e))
#     return new_list

# result = f(lambda x: x**2, [1,2,3,4,5], lambda x: x%2 == 0)
# print(result)

# non_primes = [x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))]
# print(non_primes)

# list(map(str, range(10)))

# L1 = [1, 28, 36]
# L2 = [2, 57, 9]
# for i in map(min, L1, L2):
#     print(i)

def f(L1, L2):
    """
    L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9
    """
    # Ensure L1 and L2 are of the same length
    if len(L1) != len(L2):
        raise ValueError("L1 and L2 must be of the same length")
    
    # Compute the sum of each element in L1 raised to the power of the corresponding element in L2
    result = sum([x ** y for x, y in zip(L1, L2)])
    
    return result