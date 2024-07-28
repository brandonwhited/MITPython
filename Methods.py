s = "abdckfstkcan"
#   """s and sub are non-empty strings
#         Returns the index of the last occurrence of sub in s.
#         Returns None if sub does not occur in s"""

print(s.find("x"))  # -1

print(s.find("can"))  # 9

blah = "can"
def find(s, sub):
    if s.find(sub) == -1:
        return None
    else:
        return s.find(sub)
    


print(find(s,blah))
            
        
   
    
    