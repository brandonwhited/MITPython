sum = 0

for num in range (2, 1000):
    if num % 2 != 0:
        sum += sum + num
print(sum)

