L, R, d = list(map(int, input().split(" ")))

diff=R//d - (L-1)//d

print(diff)