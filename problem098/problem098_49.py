n = int(input())
c = input().strip()
c = list(c)

ans = 0
low = 0
high = n-1

while low<high:
    if c[low] == 'W':
        
        while low<high and c[high]=='W':
            high -= 1
        
        if c[high] == 'R':
            ans+=1
            c[high], c[low] = c[low], c[high]
            
    low += 1    

print(ans)