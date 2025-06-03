number = int(input())
tall = list(map(int, input().split()))
addition = 0
for each in range(1, number):
    difference = tall[each - 1] - tall[each]
    if difference >= 0:
        addition += difference
        tall[each] += difference
print(addition)