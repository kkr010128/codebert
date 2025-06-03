import itertools

n = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

cnt = 0
p_cnt = 0
q_cnt = 0

for a in itertools.permutations(range(n)): #順列を生成して、それらに対して処理
    cnt += 1
    for i in range(len(a)):
        if a[i]+1 != p_list[i]:
            break
        if i == len(a)-1:
            p_cnt = cnt
    for j in range(len(a)):
        if a[j]+1 != q_list[j]:
            break
        if j == len(a)-1:
            q_cnt = cnt

print(abs(p_cnt - q_cnt))
