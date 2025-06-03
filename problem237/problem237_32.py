def solve(N, data):
   ret = N
   data.sort(key=lambda x: x[0] - x[1])
   most_right = float("-inf")
   for idx, d in enumerate(data):
       l, r = d[0] - d[1], d[0] + d[1]
       if not idx:
           most_right = r
           continue
       if most_right <= l:
           most_right = r
           continue
       ret -= 1
       most_right = min(r, most_right)
   return ret

if __name__ == "__main__":
    N = int(input())
    data = []

    for _ in range(N):
        data.append(list(map(int, input().split())))
    print(solve(N, data))