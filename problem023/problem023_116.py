def insert(S, string):
    S.add(string)

def find(S, string):
    if string in S:
        print 'yes'
    else:
        print 'no'

n = input()

S = set()

for i in range(n):
    tmp1, tmp2  = map(str, raw_input().split())
    if tmp1 == 'insert':
        insert(S, tmp2)
    elif tmp1 == 'find':
        find(S, tmp2)
    else:
        print 'error!'