a, b = input().split()
op = ['==', '>', '<']
result = int(a) - int(b)
if result != 0:
    result = result // abs(result)
 
print('a ' + op[result] + ' b')