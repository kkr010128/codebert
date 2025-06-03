n=int(input())
s=[n-1]
for i in range(2,n):
    s.append((n-1)//i)
t=0    
for j in s:
    t+=j
print(t)    
