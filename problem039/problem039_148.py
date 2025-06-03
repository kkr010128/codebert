val = raw_input().split()
ret = 'No'
if val[0] < val[1] < val[2]:
    ret = 'Yes'
print(ret)