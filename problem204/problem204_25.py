S = input()
Q = int(input())
reverse = 0
left = ""
right = ""
for _ in range(Q):
    q = input().split()
    if q[0]=="1":
        reverse += 1
        left, right = right, left
    if q[0]=="2" and q[1]=="1":
        if reverse%2==0: left = q[2]+left
        else: left = left+q[2]
    if q[0]=="2" and q[1]=="2":
        if reverse%2==0: right = right+q[2]
        else: right = q[2]+right
if reverse%2==1:
    left = left[::-1]
    right = right[::-1]
    S = S[::-1]
print(left+S+right)