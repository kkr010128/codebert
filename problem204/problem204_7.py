s = input()
q = int(input())
count = 0
a = []
b = []

for _ in range(q):
    Q = list(map(str, input().split()))
    if Q[0] == "1":
        count += 1
    else:
        if (int(Q[1])+count)%2 == 1:
            a.append(Q[2])
        else:
            b.append(Q[2])
    
        
a = "".join(a[::-1])
b = "".join(b)
s = a + s + b
if count%2 == 1 and count != 0:
    s = s[::-1]
print("".join(s))