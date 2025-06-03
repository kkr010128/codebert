n = map(int,list(input()))
ans = "No"

if sum(n) % 9 == 0:
    ans = "Yes"
    
print(ans)