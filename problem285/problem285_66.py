def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

def run():
    S = list(input())

    left = [0] * (len(S) + 1)

    right = [0] * (len(S) + 1)

    for i in range(len(S)):
        if S[i] == '<':
            left[i + 1] += 1 + left[i]

    for i in range(len(S) - 1, -1, -1):
        if S[i] == '>':
            right[i] = right[i + 1] + 1

    ans = [0] * (len(S) + 1)
    for i in range(len(S) + 1):
        ans[i] = max(left[i], right[i])
    print(sum(ans))

run()


