# t1 = (1,)
# t2 = (1, 'two', 3)     
# print(t1)
# print(t2)

# t1 = (1, 'two', 3)
# t2 = (t1, 3.25)
# print(t2)
# print((t1 + t2))
# print((t1 + t2)[3])
# print((t1 + t2)[2:5])



# def intersect(t1, t2):
#     """Assumes t1 and t2 are tuples
#        Returns a tuple containing elements that are in
#           both t1 and t2"""
#     result = ()
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result
# print(intersect((1, 'a', 2), ('b', 2, 'a')))

# def find_extreme_divisors(n1, n2):
#     """Assumes that n1 and n2 are positive ints
#         Returns a tuple containing the smallest common divisor > 1 and 
#           the largest common divisor of n1 & n2. If no common divisor,
#           other than 1, returns (None, None)"""
#     min_val, max_val = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1%i == 0 and n2%i == 0:
#             if min_val == None:
#                 min_val = i
#             max_val = i
#     return min_val, max_val

# min_divisor, max_divisor = find_extreme_divisors(100, 200)
# print(min_divisor, max_divisor)

# for elem in (1, 'a', 2, (3, 4)):
#     print(elem)
 
# add_these = (1,2,3,4,5)

# def mean(x):
#     """A function that calculates the mean of a ll the numbers in a tuple. 
#     Assumes integers or floats in tuples"""
#     return sum(x) / len(x)

# print(mean(add_these))
# print(len(add_these))

# L = [1, 2, 3]
# L.append(L)
# print(L is L[-1])

def append_val(val, list_1 = []):
    list_1.append(val)
    print(list_1)
    
append_val(5, list_1 =[])

