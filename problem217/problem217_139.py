N = int(input())
a = list(map(int,input().split()))

flag = True
for a_i in a:
    if a_i%2==0:
        if not (a_i%3==0 or a_i%5==0):
            flag=False

print("APPROVED" if flag else "DENIED")
