figure = ''
height, width = [int(x) for x in input().split()]
while height or width:
    pattern = '#.' * (((height+width)//2) + 1)
    for h in range(height):
            figure += pattern[h : width + h] + '\n'
    figure += '\n'
    height, width = [int(x) for x in input().split()]

print(figure[:-1])