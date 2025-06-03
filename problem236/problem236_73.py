H = int(input())
W = int(input())
N = int(input())

longer = H

if longer < W:
    longer = W
    

print(((N-1)//longer)+1)