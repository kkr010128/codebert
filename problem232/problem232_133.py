a, b = [int(i) for i in input().split()]
aa = ''.join([str(a) for v in range(b)])
bb = ''.join([str(b) for v in range(a)])
print(aa if aa < bb else bb) 