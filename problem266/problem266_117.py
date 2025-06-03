x = int(input())

x_ = divmod(x, 100)

if 5*x_[0] >= x_[1]:
    print(1)
else:
    print(0)