n = int(input())

furui = [i for i in range(10**6+2)]

ans = 9999999999999

yakusuu = []

for i in range(1,int(n**0.5)+1+1):
    
    if n%i == 0:
        
        yakusuu.append(i)
        

    
for i in yakusuu:
    
    ans = min(i+n//i,ans)
    # print(i,ans)
    
print(ans-2)
