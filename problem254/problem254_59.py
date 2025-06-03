a=int(input())
b=int(input())
s=[0 for i in range(3)]
s[a-1] = 1
s[b-1] = 1
for i in range(3):
    if s[i]==0:
        print(i+1)