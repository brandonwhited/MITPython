# def print_name(first_name, last_name, reverse): 
#    if reverse:
#       print(last_name + ', ' + first_name)
#    else:
#       print(first_name, last_name)

def multiply(x, y = None):
    if y is not None:
        print(x * y)
    else:
        print(x)
        
multiply(5,3)