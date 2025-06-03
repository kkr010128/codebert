N,K = list(map(int,input().split()))
P = list(map(int,input().split()))

def bubblesort(l):
    for index in range(len(l)-1, 0, -1):
        for low in range(index):
            if l[low] > l[low+1]:
                tmp = l[low+1]
                l[low+1] = l[low]
                l[low] = tmp
    return l

bubblesort(P)
sum = 0
for i in range(K):
	sum = sum + P[i]
print(sum)