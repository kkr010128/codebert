#154_C
def has_duplicates(seq):
    return len(seq) != len(set(seq))

n = int(input())
a = list(map(int, input().split()))

if has_duplicates(a):
    print('NO')
else:
    print('YES')