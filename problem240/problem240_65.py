def solve():
    N,M = [int(i) for i in input().split()]
    solved = set([])
    penalty = {}
    for i in range(M):
        problem_id,result = input().split()
        if result == 'AC':
            solved.add(problem_id)
        elif result == 'WA' and problem_id not in solved:
            penalty[problem_id] = penalty.get(problem_id, 0) + 1
    num_penalties = 0
    for problem_id in solved:
        num_penalties += penalty.get(problem_id, 0)
    print(len(solved), num_penalties)


if __name__ == "__main__":
    solve()