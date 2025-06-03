k = int(input())
a, b = list(map(int, input().split()))
p = 0
while p <= 1000:
    if a <= p <= b:
        print("OK")
        exit()
    p += k
print("NG")
