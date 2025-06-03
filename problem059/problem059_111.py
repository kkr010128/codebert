r,c = map(int,input().split())
rc = list([int(x) for x in input().split()] for _ in range(r))
[rc[i].append(sum(rc[i])) for i in range(r)]
rc.append([sum(i) for i in zip(*rc)])

for col in rc: print(*col)