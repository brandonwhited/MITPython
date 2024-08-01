# def get_min(d):
#     # Step 1: Extract all keys from the dictionary
#     keys = d.keys()
    
#     # Step 2: Find the key that comes first alphabetically
#     min_key = min(keys)
    
#     # Step 3: Return the value associated with this key
#     return d[min_key]

# # Example usage
# d = {'x': 11, 'b': 12}
# print(get_min(d))  # Output: 12



d = {'x': 10, 'y': 20, 'z': 30}
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

print(d['x'])

print(d.get('x', 20))