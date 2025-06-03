x=int(input())
kosu=0
for i in range(1000):
    kosu+=1
    if 100*kosu<=x<=105*kosu:
        print(1)
        quit()
print(0)