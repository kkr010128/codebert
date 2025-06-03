n = int(input())
m = [[0 for j in range(n)] for i in range(n)]
color = [0 for i in range(n)]
d = [0 for i in range(n)]
f = [0 for i in range(n)]
time = [0]


def dfs(u):
    color[u] = 1
    time[0] += 1
    d[u] = time[0]
    for i in range(n):
        if m[u][i] == 1 and color[i] == 0:
            dfs(i)

    color[u] = 2
    time[0] += 1
    f[u] = time[0]


def main():
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(2, len(data)):
            m[data[0]-1][data[j]-1] = 1

    for i in range(n):
        if color[i] == 0:
            dfs(i)

    for i in range(n):
        print(i+1, d[i], f[i])


if __name__ == '__main__':
    main()

