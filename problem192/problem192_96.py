N = int(input())
Alist = list(map(int, input().split()))

n_dic = {}
for a in Alist:
    if a in n_dic.keys():
        n_dic[a] += 1
    else:
        n_dic[a] = 1

base = 0
for k, v in n_dic.items():
    base += v * (v-1) // 2


for k in range(N):
    n = n_dic[Alist[k]] - 1
    print(base - n)
