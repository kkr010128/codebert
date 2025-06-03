import sys
import math
import itertools
# num = []
# for e in sys.stdin:
#     num.append(map(int, e.split()))

N = int(input())

count = []
for i in range(N):
    count.append(0)

max = min(int(math.sqrt(N)), int(N/2))
l = []

for i in range(1, max+1):
    l.append(i)

h = itertools.combinations_with_replacement(l, 3)

# print(h)
for i,j,k in h:
    n = (i+j+k)**2 - i*j - j*k - k*i
    # print(n)

    if(n <=N):
        if(i==j==k):
            count[n-1]+=1
        elif(i==j or j==k or i == k):
            count[n-1]+=3
        else:
            count[n-1]+=6


for c in count:
    print(c)

# for n in range(1, N+1):
#     count = 0;
#     max = min(int(math.sqrt(n)), int(n/2))
#     l = []
#
#     for i in range(1, max+1):
#         l.append(i)
#
#     h = list(itertools.combinations_with_replacement(l, 3))
#     for i,j,k in h:
#         if n == (i+j+k)**2 - i*j - j*k - k*i:
#             if(i==j==k):
#                 count+=1
#             elif(i==j or j==k or i == k):
#                 count+=3
#             else:
#                 count+=6

    # for i in range(1, max+1):
    #     for j in range(1, max+1):
    #         for k in range(1, max+1):
    #             num = i**2 + j**2 + k**2 + i*j + j*k + k*i
    #             if n == num:
    #                 count+=1
    # print(count)


    # print(max)


    # l = []
    #
    # for i in range(1, max+1):
    #     l.append(i)
    #
    # # h = itertools.combinations_with_replacement(l, 3)
    #
    # for i,j,k in h:
    #     if n == i**2 + j**2 + k**2 + i*j + j*k + k*i:
    #         if(i==j==k):
    #             count+=1
    #         elif(i==j or j==k or i == k):
    #             count+=3
    #         else:
    #             count+=6
    # print(count)
