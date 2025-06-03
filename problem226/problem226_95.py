H, N = map(int,input().split())
special_move = list(map(int,input().split()))

if H <= sum(special_move):
    result = 'Yes'
else:
    result = 'No'

print(result)