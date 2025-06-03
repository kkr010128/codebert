n = int(input())
playlists = []

for _ in range(n):
    title, playtime = input().split()
    playlists.append([title, int(playtime)])

titles, playtimes = list(zip(*playlists))
lastmusic = input()

lastmusic_timing = titles.index(lastmusic)
print(sum(playtimes[lastmusic_timing + 1:]))