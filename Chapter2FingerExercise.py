c = 0
n = 0
l = 0
 


while c < 10:
	l = int(input("Please type in an integer 10 times "))
	if l % 2 != 0:
		if l > n:
			n = l
	c = c + 1

if n == 0:
	print("There are no odd numbers")
else:
	print(n)


#while c < 10:
#	l = int(input("Please type in an integer 10 times "))
#	c = c + 1