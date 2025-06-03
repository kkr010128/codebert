nn = int(input())
aa = list(map(int,input().split()))

joushi = [0]*nn

for i in range(len(aa)):
    joushi[aa[i]-1] += 1

for j in range(len(joushi)):
    print(joushi[j])
