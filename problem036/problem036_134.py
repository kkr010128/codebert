#AOJ ITP1_1_C

N = input().split()
area = 0
perimeter = 0

length=int(N[0])
breadth=int(N[1])

area = length * breadth
perimeter = (length + breadth) * 2

print(str(area)+" "+str(perimeter) )
