a=str(input())
b=''

for i in range(len(a)):
    if a[i].isupper():
        b+=a[i].lower()
    elif a[i].islower:
        b+=a[i].upper()
        
print(b)
        
