# coding: utf-8
# Your code here!
dic = set()
def insert(s):
    dic.add(s)
def find(s):
    if s in dic:
        print("yes")
    else:
        print("no")
i = int(input())
for c in range(i):
    op,s = map(str,input().split())
    if op == "insert":
        insert(s)
    elif op == "find":
        find(s)
