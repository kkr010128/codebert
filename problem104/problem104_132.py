l, r, d = [int(x) for x in input().rstrip().split(" ")]
print(r//d-l//d + (l%d==0))