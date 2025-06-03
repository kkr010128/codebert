even,odd = map(int, input().split())

  
print(int(even * (even-1)/2 + odd * (odd-1)/2))
