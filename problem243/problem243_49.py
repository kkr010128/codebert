N = int(input())
music = []
for i in range(N):
    music.append(input().split())
X = (input())
Time = 0
kama = False
for s,t in music:
    if kama:
        Time += int(t)
    if s == X:
        kama = True
            
print(Time)