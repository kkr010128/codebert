import sys
import math
import itertools
import collections

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N = NI()
    xy = [NLI() for _ in range(N)]
    
    ls = [p for p in range(N)]
    p_list = list(itertools.permutations(ls))
    
    full_course = ["" for _ in range(len(p_list))]
    
    for k in range(len(p_list)):
        distance = 0
        for l in range(N-1):
            departure = p_list[k][l] 
            goal = p_list[k][l+1]
            Xd = xy[departure][0]
            Yd = xy[departure][1]
            Xg = xy[goal][0]
            Yg = xy[goal][1]
            distance += ((Xd-Xg)**2 + (Yd-Yg)**2)**(1/2)
        full_course[k] = distance

    print(sum(full_course)/len(p_list))


if __name__ == '__main__':
    main()