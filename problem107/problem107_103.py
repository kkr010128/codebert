from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

pc_memo = defaultdict(int)
memo = defaultdict(int)


def to_next(x):
    if x not in pc_memo.keys():
        pc_memo[x] = x % "{:b}".format(x).count('1')
    return pc_memo[x]


def f(x):
    if x == 0:
        return 0
    if x not in memo.keys():
        memo[x] = f(to_next(x))+1
    return memo[x]


for i in range(2*10**5):
    f(i)

n = int(input())
x = input().rstrip()
one_cnt = x.count('1')

mod_minus = 0
mod_plus = 0
for i, a in enumerate(reversed(x)):
    if a == '1':
        if 0 < one_cnt-1:
            mod_minus += pow(2, i, one_cnt-1)
            mod_minus %= one_cnt-1
        mod_plus += pow(2, i, one_cnt+1)
        mod_plus %= one_cnt+1


for i in range(n):
    if x[i] == '0':
        nx = mod_plus+pow(2, n-i-1, one_cnt+1)
        nx %= one_cnt+1
        print(f(nx)+1)
    else:
        if 0 < one_cnt-1:
            nx = mod_minus-pow(2, n-i-1, one_cnt-1)
            nx %= one_cnt-1
            print(f(nx)+1)
        else:
            print(0)
