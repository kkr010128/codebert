N = int(input())
A = list(map(int, input().split()))

flag = True
for n in A:
    if n % 2 == 0 and (n % 3 != 0 and n % 5 != 0):
        flag = False
print("APPROVED" if flag else "DENIED")
