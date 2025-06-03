import itertools
N = int(input())
L = list(map(int,input().split()))
tri_list = list(itertools.combinations(L,3))
num = 0
for i in range(len(tri_list)):
    combi = tri_list[i]
    if (combi[0] != combi[1]) and (combi[1] != combi[2]) and (combi[2] != combi[0]):
        if ((abs(combi[0] - combi[1])) < combi[2]) and (combi[2] < (combi[0] + combi[1])):
            num += 1
print(num)