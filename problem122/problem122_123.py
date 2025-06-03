n = int(input())
a = list(map(int, input().split()))
s = sum(a)
q = int(input())
l = [0] * 100000
for i in a:
    l[i-1] += 1
for i in range(q):
    x,y = map(int, input().split())
    hoge = l[x-1]
    s -= hoge*x
    s += hoge*y
    l[y-1] += hoge
    l[x-1] = 0
    print(s)
    
