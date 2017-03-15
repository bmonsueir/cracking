# check id if permutaion is a palindrome

def is_palidrime(a):
    count = 0
    a = list(a)
    for i in a:
        if a.count(i) % 2 != 0:
            count += 1
    if count > 1:
        return False
    else:
        return True
        
a = raw_input("enter string: ")
print is_palidrime(a)