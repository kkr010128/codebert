a= input()
c=""
for i in range(0, len(a)):
    if a[i]=="?":
        c=c+"D"
    else:
        c=c+a[i]
print(c)