w=input().lower()
list=[]
while True:
    s=input()
    if s=="END_OF_TEXT":
        break
    c=s.lower().split().count(w)
    list.append(c)
print(sum(list))
