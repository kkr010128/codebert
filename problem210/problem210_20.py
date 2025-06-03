import sys
from copy import copy, deepcopy
input = sys.stdin.readline
'''
n, m = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
S = input().strip()
for CASES in range(int(input())):
'''
inf = 100000000000000000  # 1e17
mod = 998244353

'''
# example input


'''


def replace(pos, char):
    x = pos
    old_char = A[x]
    while x <= n:
        tr[x][old_char] -= 1
        x += x & (-x)
    x = pos
    while x <= n:
        tr[x][char] += 1
        x += x & (-x)
    A[pos] = char


def query(pos, char):
    x = pos
    sum = 0
    while x != 0:
        sum += tr[x][char]
        x -= x & (-x)
    return sum


n = int(input())
S = input().strip()
A = [27] * (n + 1)
'''
for i in range(len(S)):
    A.append(ord(S[i])-ord('a'))
'''
tr = [[0] * 30 for i in range(len(S) + 10)]
for i in range(len(S)):
    replace(i + 1, ord(S[i]) - ord('a'))
q = int(input())
for i in range(q):
    QUERY = list((input().split()))
    if int(QUERY[0]) == 1:
        replace(int(QUERY[1]), ord(QUERY[2]) - ord('a'))
    else:
        sum = 0
        for char in range(ord('a'), ord('z') + 1):
            num = query(int(QUERY[2]), char - ord('a')) - \
                query(int(QUERY[1]) - 1, char - ord('a'))
            if num >= 1:
                sum += 1
        print(sum)
