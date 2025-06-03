from itertools import accumulate 

n = int(input())
song= []
time = []

for i in range(n):
    s, t = input().split()
    song.append(s)
    time.append(int(t))

time_acc = list(accumulate(time))
x = input()

print(time_acc[n - 1] - time_acc[song.index(x)])