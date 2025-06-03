def attacks(HP, times=1):
    if HP==0: return times-1
    
    HP //= 2
    times *= 2
    return attacks(HP,times)

h=int(input())

print(attacks(h))
