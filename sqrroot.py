#x = .25
#episolon = 0.01
#step = episolon**2  
#num_guesses = 0
#ans = 0.0
# while abs(ans**2 - x) >= episolon and ans*ans <= x:
#     ans += step
#     num_guesses += 1
# print('num_guesses =', num_guesses)
# if abs(ans**2 - x) >= episolon:
#     print('Failed on square root of', x)
# else:  
#     print(ans, 'is close to square root of', x) 

x = -25
episilon = 0.01
num_guesses, low = 0,0 
high = max(1,x)
ans = (high + low)/2
while abs(ans**2 - x) >= episilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print("number of guesses= ", num_guesses)
print(ans, 'is close to square root of', x)



