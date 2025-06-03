n = int(input())
titles = []
times = []
for i in range(n):
    title,m = input().split()
    titles.append(title)
    times.append(int(m))
print(sum(times[titles.index(input())+1:]))