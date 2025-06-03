import collections
N = int(input())
A = list(map(int,input().split()))

#index,h
pp =[]
pm = []
all_set = set()
for i in range(N):

    pp.append(i + A[i])
    pm.append( i - A[i])

count = 0
c = collections.Counter(pp)
#print(c)
for i in range(N):
    count += c[pm[i]] 
    #print(c[pm[i]])

    #count += pp.count(pm[i])
    #count += pm.count(pp[i])

print(count)