a,b=[],[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    a+=[x-y]
    b+=[x+y]
print(max(max(a)-min(a),max(b)-min(b)))