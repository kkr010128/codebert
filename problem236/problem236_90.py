h = int(input())
w = int(input())
n = int(input())

lines = 0
act = 0

if h <= w:
#     print('w long')
    lines = h
    act = w
else:
#     print('h long')
    lines = w
    act = h
    
# print(lines)
# print(act)
    
draw = 0 
for i in range(lines):
    
    if n <= (i + 1) * act:
        print(i + 1)
        break