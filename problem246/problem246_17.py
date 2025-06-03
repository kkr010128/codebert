from itertools import permutations
if __name__ == "__main__":
    N = int(input())
    P = tuple(map(int,input().split()))
    Q = tuple(map(int,input().split()))
    arr = [i for i in range(1,N+1)]
    pattern_arr = list(permutations(arr))
    a,b = -1,-1
    for i,pattern in enumerate(pattern_arr):
        if pattern == P:
            a = i
        if pattern == Q:
            b = i
    print(abs(a-b))