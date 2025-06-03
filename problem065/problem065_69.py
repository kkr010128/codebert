W=input()
a=0
while True:
    T=input()
    if T=='END_OF_TEXT':
        break
    else:
        a +=T.lower().split().count(W)
print(a)
