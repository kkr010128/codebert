n = int(input())
playlist = []
duration = []

for i in range(n):
    s, t = input().split()
    playlist.append(s)
    duration.append(int(t))

index = playlist.index(input())

durations = sum(duration[index + 1: ])
print(durations)