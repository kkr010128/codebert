n = int(input())
found = False

for i in range(1, n + 1):
    x = int ( i * 1.08 )
    if x == n :
        print(i)
        found = True
        break

if not found:
    print(":(")