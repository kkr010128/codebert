M,D=map(int, input().split())
MM,DD=map(int, input().split())

if MM-1==M or (MM-1==0 and M==12):
    print(1)
else:
    print(0)