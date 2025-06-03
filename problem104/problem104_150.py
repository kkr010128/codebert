l, r, d = map(int, input().split())
print(r//d-l//d+int(l%d==0 and r%d==0))