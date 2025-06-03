def ans():
    if t==0:
        return "N0"
    if d/s <= t:
        return "Yes"
    else:
        return "No"
        
d, t, s = map(int, input().split())
print(ans())