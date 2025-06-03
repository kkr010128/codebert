nMonsters, nSpecial = [int(x) for x in input().split()]

monst = [int(x) for x in input().split()]

monst.sort()

nMonsters -= nSpecial

if nMonsters < 0:
    print(0)
else:
    print(sum(monst[0:nMonsters]))
