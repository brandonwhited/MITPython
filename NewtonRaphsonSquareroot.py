#x = 0.0 
#for i in range(10):
#    x += 0.1
#if x == 1.0:
#    print(f'{x} - 1.0')
#else:
#    print(f'{x} is not 1.0')
#k = 25.0
#epsilon = 0.01
#guess = k/2 
#while abs(guess**2 - k) >= episilon:
#    guess = guess - (((guess**2) - k)/(2*guess))
#print(f'Square root of {k} is about {guess}')
x1 = 25
epsilon = 0.01
if x1 < 0:
    print('Sorry, no square root')
else:
    low = 0
    high = max(1, x1)
    ans = (high + low) / 2
    while abs(ans**2 - x1) >= epsilon:
        print(ans**2 - x1, epsilon,   low,   high,   ans)
        if ans**2 < x1:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
x1_root = ans
print(x1_root)
# THIS PROGRAMS OUTPUTS ARE VERY VERY WEIRD 

