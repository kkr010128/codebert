
n = int(input())
songs = []

for i in range(n):
    s,t = map(str,input().split())
    t = int(t)
    songs.append([s,t])
x = input()
number = 0

for i in range(n):
    if songs[i][0] == x:
        number = i + 1
#print("number: " + str(number))

ans = 0
for j in range(number,n):
    ans += songs[j][1]
print(ans)
