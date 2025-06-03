w=input()
ll=list()
while True:
    T=input()
    if T=="END_OF_TEXT":
        break
    T=T.lower()
    t=T.split()
    for i in t:
        ll.append(i)
ans=ll.count(w)
print(ans)

