N = int(input())
n_list = []
count = 1
max_val = 1
res = 0
for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            res = x**2 +y**2 + z**2 + x*y + y*z + z*x
            for i in range(int(x!=y) + int(y!=z) + int(z!=x)-1):
                count *= 3-i
            if max_val < res:
                for i in range(max_val, res+1):
                    if i != res: n_list.append(0)
                    else: n_list.append(count)
                max_val = res+1
            else:
                n_list[res-1] += count
            count = 1

            

for i in range(N):
    print(n_list[i])
