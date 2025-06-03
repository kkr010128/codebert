s = input()

x = ""
y = ""

Q = int(input())

rev = 0
for i in range(Q):
    q = list(input().split())
    
    if q[0] == "2":
        q[1] = int(q[1])
        q[1] -= 1 
        
        if rev:
            q[1] = 1 - q[1]
        
        if q[1] == 0:
            x += q[2]
        else:
            y += q[2]
    else:
        rev = 1 - rev
        
x = x[::-1]
ans = x + s + y

if rev:
    ans = ans[::-1]

print(ans)