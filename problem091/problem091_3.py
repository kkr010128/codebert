# -*- coding: utf-8 -*-

def judge_tri(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False

N = int(input())
L = map(int, input().split())

cnt = 0
L_sort = sorted(L)
for i in range(N):
    for j in range(i+1, N, 1):
        if L_sort[i] != L_sort[j]:
            for k in range(j+1, N, 1):
                if L_sort[i] != L_sort[k] and L_sort[j] != L_sort[k]:
                    if judge_tri(L_sort[i], L_sort[j], L_sort[k]):
                        cnt += 1

print(cnt)