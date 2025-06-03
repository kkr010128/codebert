import math

def main():
    n = int(input())
    A = list(map(int, input().split()))

    max_node = [0 for i in range(n+1)]
    min_node = [0 for i in range(n+1)]
    res = 0

    for i in range(n, -1, -1):
        if i == n:
            max_node[i] = A[i]
            min_node[i] = A[i]
        elif i == 0:
            max_node[i] = 1
            min_node[i] = 1
        elif i == 1 and n != 1:
            max_node[i] = 2
            min_node[i] = math.ceil(min_node[i+1] /2) + A[i]
        else:
            max_node[i] = max_node[i+1] + A[i]
            min_node[i] = math.ceil(min_node[i+1] / 2) + A[i]

    for i in range(n):
        if i == 0:
            if n != 0 and A[i] != 0:
                res = -1
                break
        else:
            if max_node[i] > 2 * (max_node[i-1] - A[i-1]):
                max_node[i] = 2 * (max_node[i-1] - A[i-1])
            if max_node[i] < min_node[i]:
                res = -1
                break
    
    if res == -1:
        print(res)
    else:
        if n == 0 and A[i] != 1:
            print(-1)
        else:
            print(sum(max_node))

if __name__ == '__main__':
    main()