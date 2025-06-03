import itertools,numpy as np,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
A = LI()
sum_A = sum(A)
accumulate_A = np.array(list(itertools.accumulate(A)))
sub_A1 = sum_A-accumulate_A
sub_A2 = sum_A-sub_A1
print(np.abs(sub_A1-sub_A2).min())
