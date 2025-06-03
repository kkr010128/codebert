t = int(input())

for i in range(8):
    if (400+200*i) <= t <= (599 + 200*i):
        print(8-i)
