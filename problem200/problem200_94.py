A,B,M=[int(i) for i in input().split() ]
a = [int(i) for i in input().split() ]
b = [int(i) for i in input().split() ]

mlist = []
for i in range(M):
  mlist.append( [ int(i) for i in input().split() ] )

print( min(min(a) + min(b),  min( [a[i[0]-1] + b[i[1]-1] - i[2] for i in mlist ])))
