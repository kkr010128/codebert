S,T=map(str,input().strip().split())
A,B=map(int,input().strip().split())
U=input()

if U==S:
    print("{} {}".format(A-1,B))
else:
    print("{} {}".format(A,B-1))