#get input
n = input()
S = map(lambda x: int(x), input().split(' '))
q = input()
T = list(map(lambda x: int(x), input().split(' ')))

#create T set
T_set = set(T)

#iterate S and counting
count = 0
for i in S:
    if i in T_set:
        count += 1
        T_set.remove(i)

print(count)
