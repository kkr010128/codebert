K = int(input())
A, B = map(int, input().split())
for i in range(0, B+1, K):
    if i >= A:
        print("OK")
        exit()
print("NG")
