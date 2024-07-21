sum = 5
for num in range (4,999):
    #if num % 2 == 0:
        #continue
    for divisor in range(2,int(num**.5) + 1):
        #print(num, divisor, sum,sum - num )
        if num % divisor == 0:
            break
        #Checks to see if number is composite/has other factors.
        if num % divisor != 0 and divisor == (int(num**.5)):
        #
              sum = sum + num 
              print(num, sum)
        #else:
            #sum = sum + num
            



