import itertools

def check(targets):
    if targets[1] > targets[0] and targets[2] > targets[1]:
        return True
    else:
        return False


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    K = int(input())
    targets = [A, B, C]
    answer = 'No'

    cases = itertools.product([0, 1, 2], repeat=K)
    for case in cases:
        copy_targets = targets.copy()
        for i in case:
            copy_targets[i] = copy_targets[i] * 2
        if check(copy_targets):
            answer = 'Yes'
            break

    print(answer)