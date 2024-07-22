def find_root(x, power, epsilon):
    #Find interval containing answer
    if x < 0 and power%2 == 0:
        return None # negative number has no even-powered roots
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans
print(find_root(25, 2, .001))

print(find_root(-8, 3, .001))
print(find_root(16, 4, .001))




def is_in(string1, string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False

print(is_in('hello', 'hello world'))
#Write a function is_in that accepts two strings 
# as arguments and returns True if either string occurs 
# anywhere in the other, and False otherwise. 
# Hint: you might want to use the built-in str operator in.

def test_is_in():