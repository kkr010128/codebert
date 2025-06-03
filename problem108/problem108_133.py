N = input()
for i in range(1,12):
    if i * 1000 - int(N) < 0:
        continue
    else:
        print(i * 1000 - int(N))
        break