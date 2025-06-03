from collections import deque

def main():
    n = int(input())
    l = list(map(int, input().split()))

    comfort = 0
    l_sorted = sorted(l, reverse=True)
    q = deque([l_sorted[0]])
    for i in range(1, n):
        comfort += q[0]
        q.popleft()
        for _ in range(2):
            q.append(l_sorted[i])
    print(comfort)

if __name__ == '__main__':
    main()
