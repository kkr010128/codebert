n=int(input())

an=0
for j in range(1,n):
    an+=int((n-1)/j)    
print(an)