n=int(input())
s=list(input())
num=0
if n<3:
    exit()
for i in range(n-2):
    if (s[i]=="A") and (s[i+1]=="B") and (s[i+2]=="C"):
        num+=1
print(num)
