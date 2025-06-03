import math
while True:
    n = int(input())
    if n == 0:
        break
    dset = list(map(int, input().split()))
    mean = sum(dset)/len(dset)
    sigma = math.sqrt(sum([(x-mean)**2 for x in dset])/len(dset))
    print('%.06f' % sigma)