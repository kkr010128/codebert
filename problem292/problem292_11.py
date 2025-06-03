input()
*l,=map(int,input().split())
print((pow(sum(l),2)-sum([pow(x,2) for x in l]))//2)