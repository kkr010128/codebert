numz = input()
count = 0
numz_pair = numz.split(" ")
numz_pair = list(map(int, numz_pair))

for i in range(len(numz_pair)):
    if numz_pair[i] <= 9:
        count = count + 1
    else:
        print(-1)
        break

if count == len(numz_pair):
    print(numz_pair[0]*numz_pair[1])
