import itertools
n = int(input())
l = list(map(int, input().split()))    
count = 0
ind_list = list(itertools.combinations(range(0,n), 3))

for ind in ind_list:
    if (l[ind[0]]+l[ind[1]])>l[ind[2]] and (l[ind[1]]+l[ind[2]])>l[ind[0]] and (l[ind[2]]+l[ind[0]])>l[ind[1]]:
        if l[ind[0]]!=l[ind[1]] and l[ind[0]]!=l[ind[2]] and l[ind[1]]!=l[ind[2]]:
            count += 1

print(count)