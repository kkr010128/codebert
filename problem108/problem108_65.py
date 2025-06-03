n = int(input())
k = int((n/1000)+1)*1000
print(0 if n%1000 == 0 else (k-n))
