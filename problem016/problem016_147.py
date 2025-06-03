# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C
# Stable Sort
# Result:
# Modifications
# - modify inner loop start value of bubble_sort
#   This was the cause of the previous wrong answer.
# - improve performance of is_stable function
import sys

ary_len = int(sys.stdin.readline())
ary_str = sys.stdin.readline().rstrip().split(' ')
ary = map(lambda s: (int(s[1]), s), ary_str)

# a is an array of tupples whose format is like (4, 'C4').
def bubble_sort(a):
    a_len = len(a)
    for i in range(0, a_len):
        for j in reversed(range(i + 1, a_len)):
            if a[j][0] < a[j - 1][0]:
                v = a[j]
                a[j] = a[j - 1]
                a[j - 1] = v

# a is an array of tupples whose format is like (4, 'C4').
def selection_sort(a):
    a_len = len(a)
    for i in range(0, a_len):
        minj = i;
        for j in range(i, a_len):
            if a[j][0] < a[minj][0]:
                minj = j
        if minj != i:
            v = a[i]
            a[i] = a[minj]
            a[minj] = v

def print_ary(a):
    vals = map(lambda s: s[1], a)
    print ' '.join(vals)

def is_stable(before, after):
    length = len(before)
    for i in range(0, length):
        for j in range(i + 1, length):
            if before[i][0] == before[j][0]:
                v1 = before[i][1]
                v2 = before[j][1]
                for k in range(0, length):
                    if after[k][1] == v1:
                        v1_idx_after = k
                        break
                for k in range(0, length):
                    if after[k][1] == v2:
                        v2_idx_after = k
                        break
                if v1_idx_after > v2_idx_after:
                    return False
    return True

def run_sort(ary, sort_fn):
    ary1 = list(ary)
    sort_fn(ary1)
    print_ary(ary1)
    if is_stable(ary, ary1):
        print 'Stable'
    else:
        print 'Not stable'

### main
run_sort(ary, bubble_sort)
run_sort(ary, selection_sort)