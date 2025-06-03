import sys
dic = set()
L = sys.stdin.readlines()

for Ins in L[1:]:
    ins, op = Ins.split()
    if ins == 'insert':
        dic.add(op)
    if ins == 'find':
        print('yes' if op in dic else 'no')