S = list(input().split())
a = []

kazu = []
for i in range(1+10**6):
    kazu.append(str(i))


for i in range(len(S)):
    if S[i] in kazu:
        a.append(int(S[i]))

    elif S[i] == "+":
        x = a.pop()
        y = a.pop()
        a.append(x+y)
    
    elif S[i] == "-":
        x = a.pop()
        y = a.pop()
        a.append(y-x)

    elif S[i] == "*":
        x = a.pop()
        y = a.pop()
        a.append(x*y)
        
print(a[0])

