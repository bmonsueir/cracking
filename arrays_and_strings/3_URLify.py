# replace spaces with %20

def urlify(a):
    a = list(a)
    for i in range(len(a)):
        if a[i] == " ":
            a[i] = "%20"
    return "".join(a)
    
a = raw_input("enter the string: ")

print urlify(a)