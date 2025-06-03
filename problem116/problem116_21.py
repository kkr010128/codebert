s=list(input())
t=list(input())
s_length=len(s)
t_length=len(t)
#print(s[3])
#print(t[3])

count=0
for i in range(s_length):
    if s[i]!=t[i]:
        count+=1
print(count)