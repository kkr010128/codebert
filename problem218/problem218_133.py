N = int(input())
S = [input() for i in range(N)]

dict = {}

for s in S :
    dict.setdefault(s, 0)
    dict[s] += 1

max_value =  max(dict.values())
ans = sorted([ k for k,v in dict.items() if v == max_value])

for a in ans :
    print(a)