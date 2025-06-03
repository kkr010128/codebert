#coding:utf-8

N = int(input())
buff = [y for x in range(N) for y in [input().split()]]
data = [(x[0], int(x[1])) for x in buff]
S = [x for x in data if x[0]=="S"]
H = [x for x in data if x[0]=="H"]
D = [x for x in data if x[0]=="D"]
C = [x for x in data if x[0]=="C"]

ansS = [("S", x) for x in range(1,14) if ("S", x) not in S]
ansH = [("H", x) for x in range(1,14) if ("H", x) not in H]
ansD = [("D", x) for x in range(1,14) if ("D", x) not in D]
ansC = [("C", x) for x in range(1,14) if ("C", x) not in C]

ans = ansS + ansH + ansC + ansD
[print(str(x[0]) + " " + str(x[1])) for x in ans]