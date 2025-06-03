n = int(input())
st = [input().split() for _ in range(n)]
x = input()

s,t = zip(*st)

print(sum(int(t[i]) for i in range(s.index(x)+1,n)))
