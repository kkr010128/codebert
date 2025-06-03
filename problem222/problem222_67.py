input()
(*a,) = map(int, input().split())
print(["NO", "YES"][len(a) == len(set(a))])