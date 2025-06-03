X = int(input())

for i in range(100000//100 +1):
    if X >= i*100 and X<= i*105:
        print(1)
        exit()
print(0)
