import copy

# L = [2]
# L1 = [L]
# L2 = L1[:]
# L2 = copy.deepcopy(L1)
# L.append(3)
# print(f'L1 = {L1}, L2 = {L2}')

L1 = [2]
L2 = [L1, L1]
L3 = copy.deepcopy(L2)
L3[0].append(3)
print(L3)