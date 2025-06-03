def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += j
    
    return table
  
n=int(input())
print(sum(num_divisors_table(n)))