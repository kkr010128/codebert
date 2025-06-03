# -*- coding: utf-8 -*-

s, t = map(str, input().split())
a, b = map(int, input().split())
u = str(input())

dic = {s:a, t:b}

dic[u] = dic[u] - 1

print(dic[s], dic[t])