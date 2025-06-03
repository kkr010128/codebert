n = int(input())
s = input()
#print(n , s , ' ')
p = "ABC"
ans = 0

for i in range(n - 2):
            if s[i : (i + 3)] == p :
                  ans += 1
print(ans)                
            
