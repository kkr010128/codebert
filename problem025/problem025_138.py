n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
memo = [[None]*2000 for i in range(2000)]


def exhaustivesearch(i, target):
    if memo[i][target] is not None:
        return memo[i][target]
    if target == 0:
        memo[i][target] = True
        return True
    if i >= n:
        memo[i][target] = False
        return False
    else:
        memo[i][target] = exhaustivesearch(i + 1, target) or exhaustivesearch(i + 1, target-A[i])
        return memo[i][target]


for j in m:
    if exhaustivesearch(0, j):
        print("yes")
    else:
        print("no")