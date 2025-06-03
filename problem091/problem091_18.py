def backtrack(nums, step, result):
    if len(step) == 3:
        if len(set(step)) == 3:
            sorted_step = sorted(step)
            a,b,c = sorted_step
            if a+b > c:
                result.append(step[:])
    else:
        for i in range(len(nums)):
            step.append(nums[i])
            backtrack(nums[i+1:], step, result)
            step.pop()

def solve():
    N = int(input())
    L = [int(i) for i in input().split()]
    result = []
    backtrack(L, [], result)
    print(len(result))

if __name__ == "__main__":
    solve()