A, B = map(int, input().split())
H = list(map(int, input().split()))
 
print(len([1 for h in H if h >= B]))