import collections
N = int(input())
A = list(map(int,input().split()))
count = collections.Counter(A) #こいつは辞書型みたいなもん
sum = 0
for x in count.values():
    sum += x*(x-1)//2
for x in A:
    print(sum-(count[x]-1))