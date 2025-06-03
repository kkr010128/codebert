S = input()
Q = int(input())
q = []
for i in range(Q):
    a = input().split(" ")
    if len(a) == 1:
        q.append([int(a[0])])
    else:
        q.append([int(a[0]), int(a[1]), a[2]])

#print(S)
#print(q)

def switch(s):
    d = ""
    for i in range(len(s)):
        d += s[len(s) - i - 1]
    return d

H = ""
B = ""

direction = 1 #通常の向き　-1:反対方向

for t in range(len(q)):
    T = q[t]
    if T[0] == 1:
        direction *= -1
    else:
        F = T[1]
        C = T[2]
        if F == 1:
            if direction == 1:
                H += C
            else:
                B += C
        else:
            if direction == 1:
                B += C
            else:
                H += C

if direction == 1:
    print(switch(H) + S + B)
else:
    print(switch(B) + switch(S) + H)