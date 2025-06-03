kyu = [2000, 1800, 1600, 1400, 1200, 1000, 800, 600, 400, 0]
x = int(input())
for k, num in enumerate(kyu):
    if num > x >= kyu[k+1]:
        print(k + 1)
        break