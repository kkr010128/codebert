N = int(input())


for i in range(10):
    if i==0:
        continue
    else:
        i_pair = N / i
        if N % i == 0 and i_pair < 10:
            print("Yes")
            exit()
            
            
print("No")