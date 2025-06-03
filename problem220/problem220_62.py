s,t = map(str, input().split())
a,b = map(int, input().split())
u = input()
print(a-1 if s==u else a, b if s==u else b-1)