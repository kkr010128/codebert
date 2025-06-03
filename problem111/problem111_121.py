n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst, reverse = True)
summ = lst[0] + 2 * sum(lst[1:n//2])
if n % 2:
    summ += lst[n//2]
print(summ)

