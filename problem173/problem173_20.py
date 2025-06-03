N = int(input())
print(sum(n for n in range(1+N) if n%3!=0 and n%5!=0))