N, K = map(int, input().split())
Hlist = list(map(int, input().split()))
Hlist = sorted(Hlist)[::-1]
#user K super attack for largest K enemy
remainHlist = Hlist[K:]
attackTimes = sum(remainHlist)
print(attackTimes)