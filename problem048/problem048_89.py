#coding:utf-8

n = input()

a = []

a_input = raw_input().split()

for i in a_input:
    a.append(int(i))

print min(a), max(a), sum(a)