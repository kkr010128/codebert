def exhaustiveSearch(A:list, m:int) -> str:
    if m == 0:
        return True
    if len(A) == 0 or sum(A) < m:
        return False
    return exhaustiveSearch(A[1:], m) or exhaustiveSearch(A[1:], m - A[0])
    


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().rstrip().split()))
    q = int(input())
    M = list(map(int, input().rstrip().split()))
    for m in M:
        if exhaustiveSearch(A, m):
            print('yes')
        else:
            print('no')
