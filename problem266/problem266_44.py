x=int(input())
syo=x//100
amari=int(str(x)[-2:])
if amari/5<=syo:
    print(1)
    exit()
print(0)