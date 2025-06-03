n = int(input())
a = list(map(int, input().split()))
b = sorted(enumerate(a), key=lambda x:x[1])
c = [b[i][0]+1 for i in range(n)]
d = [str(x) for x in c]
e = " ".join(d)
print(e)