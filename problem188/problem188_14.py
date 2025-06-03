X,Y,A,B,C=map(int,input().split())

RO=list(map(int,input().split()))
GO=list(map(int,input().split()))
TO=list(map(int,input().split()))

RO.sort()
GO.sort()

R=RO[A-X:A]
G=GO[B-Y:B]

TO.extend(R)
TO.extend(G)

TO.sort(reverse=True)

T=TO[0:X+Y]

print(sum(T))