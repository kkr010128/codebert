c=str(input())
cl=list(c)
for i in range(len(cl)):
    if cl[i].islower():
        cl[i]=cl[i].upper()
        print(cl[i],end='')
    elif cl[i].isupper():
        cl[i] =cl[i].lower()
        print(cl[i], end='')
    elif not cl[i].isalpha():
        print(cl[i], end='')
print('')