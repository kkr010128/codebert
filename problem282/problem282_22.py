
def resolve():
    n, t = map(int, input().split())
    foods = []
    limit = 0
    tt = []
    for i in range(n):
        a, b = map(int, input().split())
        foods.append((a,b))
        limit += a
        tt.append(a)
    c = max(tt) * 2
    foods.sort(key=lambda x:(x[0], -x[1]))
    limit = min(limit * 2, t * 2)
    time = [0 for _ in range(limit+c)]
    used = [0] * (limit + c)
    used[0] = 1

    for a,b in foods:
        for i in range(limit+c)[::-1]:
            if used[i] and i+a*2 < limit + c and time[i+a*2] < time[i] + b:
                time[i+a*2] = time[i] + b
                if i+a*2 < limit:
                    used[i+a*2] = 1

    print(max(time))

if __name__ == "__main__":
    resolve()
