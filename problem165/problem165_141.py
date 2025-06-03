N = int(input())
GACHA={}
for n in range(N):
  g=input()
  GACHA[g]=GACHA.get(g,0)
print(len(GACHA))