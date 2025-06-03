S = input()
k = len(S)
if k%2==1:
    print("No")
    exit()

frag = True
for i in range(0,k,2):
    if S[i]+S[i+1]!="hi":
        frag = False

if frag:
    print("Yes")
else:
    print("No")
