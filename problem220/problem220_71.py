s,t = input().split()
d={}
d[s], d[t] = map(int,input().split())
d[input()] -= 1
print(d[s],d[t])