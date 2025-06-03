# string
# a, b, c = input().split()
# str_list = list(input().split())

# number
# a, b, c = map(int, input().split())
# num_list = list(map(int, input().split()))

# lows
# str_list = [input() for _ in range(n)]

# many inputs
# num_list = []
# for i in range(n): num_list.append(list(map(int, input().split())))

n = int(input())
l = list(map(int, input().split()))

l.sort(reverse = True)

ctr = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if l[i] == l[j]:
            continue
        for k in range(j+1, n):
            if l[j] == l[k]:
                continue
            if l[i] < l[j] + l[k]:
                ctr += 1

print(ctr)