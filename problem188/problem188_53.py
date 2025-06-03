x,y,a,b,c =map(int,input().split())
p = sorted(list(map(int,input().split())))[::-1]
q = sorted(list(map(int,input().split())))[::-1]
r = (list(map(int,input().split())))

p1 = p[:x]
q1 = q[:y]
l = sum(sorted(p1+q1+r)[::-1][:x+y])
print(l)
