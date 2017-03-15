# write a function that determines if a string contains unique characters return True or False

def is_unique(a):
    arr = list(str(a))
    counts = {}
    for i in arr:
        try:
            counts[i] += 1
        except:
            counts[i] = 1
    if max(counts.values()) > 1:
        return False
    else:
        return True
        
def is_unique2(a):
    unique = True
    for i in a:
        if a.count(i) > 1:
            unique = False
    return unique  
        
        
a = raw_input("Enter a string: ")
print is_unique2(a)

