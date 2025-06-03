hp, dmg = map(int, input().split())

if hp % dmg == 0: print(int(hp//dmg))
else: print(int(hp//dmg) + 1)