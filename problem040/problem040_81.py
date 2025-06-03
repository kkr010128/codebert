def swap(m, n, items):
    x = items[n]
    items[n] = items[m]
    items[m] = x
    

ABC = input().split()

if ABC[0] > ABC[1]:
    swap(0, 1, ABC)
    if ABC[1] > ABC[2]:
        swap(1, 2, ABC)
        if ABC[0] > ABC[1]:
            swap(0, 1, ABC)
elif ABC[1] > ABC[2]:
    swap(1, 2, ABC)
    if ABC[0] > ABC[1]:
        swap(0, 1, ABC)
print(ABC[0], ABC[1], ABC[2])