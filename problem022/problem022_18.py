def liner_search(r,key):
    for x in r:
        if x == key:
            return True
    return False


N = int(input())
S = list(map(int, input().split()))
q = int(input())
Key = list(map(int, input().split()))
cnt = 0
for i in range(q):
    if liner_search(S, Key[i]):
        cnt += 1

print(cnt)