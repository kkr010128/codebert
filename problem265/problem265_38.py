import sys
n = int(input())
ans = n*100/108
for i in [int(ans), int(ans)+1]:
    if int(i*1.08) == n:
        print(i)
        sys.exit()
print(":(")
