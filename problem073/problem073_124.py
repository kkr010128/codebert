n = int(input()) - 1 # n=n-1
print(sum([(n//x - x)*2 + 1 for x in range(1, int(n**0.5) + 1)]))
