N = int(input())

for i in range(1,11):
    need = 1000 * i
    if N <= need:
        print(need - N)
        break