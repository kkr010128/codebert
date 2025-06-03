import math
a,b,c,d = map(int,input().split())

def death_time(hp,atack):
    if hp%atack == 0:
        return hp/atack
    else:
        return hp//atack + 1

takahashi_death = death_time(a,d)
aoki_death = death_time(c,b)

if aoki_death<=takahashi_death:
    print("Yes")
else:
    print("No")