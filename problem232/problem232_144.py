ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())
 
a, b = rii()

print(min(str(a) * b, str(b) * a))