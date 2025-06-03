n = input()
l = [int(i) for i in input().split()]
print(' '.join([str(min(l)),str(max(l)),str(sum(l))]))