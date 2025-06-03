n = str(input())
if n[-1] in ['2', '4', '5', '7', '9']:
    how_to_read = 'hon'
elif n[-1] in ['0', '1', '6', '8']:
    how_to_read = 'pon'
else:
    how_to_read = 'bon'
    
print(how_to_read)