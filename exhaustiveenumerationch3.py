x = int(input("Enter a number: "))
ans = 0
while ans < abs(x):
    ans = ans + 1
    print(ans, x)
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of", x, "is", ans)
