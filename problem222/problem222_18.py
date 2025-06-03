N = int(input())
A = list(map(int, input().split()))
A.sort()
Ans = "YES"
List = []
before_n = 0
for e in A:
    if e == before_n:
        Ans = "NO"
        break
    else:
        before_n=e
print(Ans)