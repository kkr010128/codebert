k=int(input())
s=list(input())
num_list=[]
if k<len(s):
    for x in range(k):
        num_list+=s[x]
        x+=1
    t=''.join(num_list)+'...'
else:
    t=''.join(s)
print(t)