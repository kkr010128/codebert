n = int(input())
print(len([i for i, j in enumerate(input().split()) if int(j)%2 == 1 and i%2 == 0]))

