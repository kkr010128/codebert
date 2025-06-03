n = int(input())

if n % 2 == 0:
    print(f'{(n/2) / n:.10f}')
else:
    print(f'{(n//2 + 1) / n:.10f}')
