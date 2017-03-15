#  return true if one string is a permuatation of the other

def is_permutation(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    return a == b
    
a, b = raw_input("enter 2 strings: ").split(" ")    
print is_permutation(a, b)