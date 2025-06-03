s = str(input())
Q = int(input())
forward = 1
front = ""
back = ""

for i in range(Q):
    q = list(input().split())
    if q[0] == "1":
        forward *= -1
    else:
        if q[1] == "1":
            if forward == 1:
                front = q[2] + front
            else:
                back = back + q[2]        
        else:
            if forward == 1:
                back = back + q[2]
            else:
                front = q[2] + front

s = front + s + back
if forward == -1:
    s = s[::-1]
print(s)