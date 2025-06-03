x = int(input())
n=100
tes = [0]
for i in range(-250,250):
    for j in range(-250,250):
        if pow(i,5) - pow(j,5) == x:
            print(str(i)+" "+str(j))
            exit()