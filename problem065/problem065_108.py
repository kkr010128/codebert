w=input()
a=0
while True:
    t=input().split()
    l=[]
    for T in t:
        l.append(T.lower())
    a+=l.count(w)
    if t[0]=="END_OF_TEXT":
        break

print(a)
