A_count = int(input());
A = [int(n) for n in input().split()];
M_count = int(input());
M = [int(n) for n in input().split()];

memo = [[None for i in range(2000)] for j in range(A_count + 1)];

def solve(start, target):
    if memo[start][target] is not None:
        return memo[start][target];
    if target == 0:
        return True;
    elif start >= A_count:
        return False;
    else:
        result = solve(start + 1, target) or solve(start + 1, target - A[start]);
        if result:
            memo[start][target] = True;
            return True;
        else:
            memo[start][target] = False;
            return False;

for m in M:
    if solve(0, m):
        print("yes");
    else:
        print("no");
