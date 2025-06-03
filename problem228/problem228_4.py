h = int(input())
layer = 0
branch_set = 0
while True :
    if h > 1 :
        h //= 2
        layer += 1
        continue
    else :
        break

for i in range(0, layer) :
    branch_set += 2 ** i

print(branch_set + 2**layer)
