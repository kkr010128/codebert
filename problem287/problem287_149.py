c = int(input())
n = 0

for i in range(1,10):
    if c /i < 10 and c %i ==0:
        n += 1
        break
    
ans = 'Yes' if n >= 1 else 'No' 
print(ans)