
x = int(input( 'Enter an integer greater than 2: '))
largest_divisor = None
Clean_Divisor_Count = 0
for guess in range(2,x+1):
    print(guess, Clean_Divisor_Count, largest_divisor)
    if x % guess == 0:
        Clean_Divisor_Count += 1
        largest_divisor = guess
if Clean_Divisor_Count > 1:
    print("Largest divisor of", x, "is", largest_divisor)
else:
    print(x, "is a prime number")   
    


