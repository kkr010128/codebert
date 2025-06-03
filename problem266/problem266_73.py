X = int(input())
num_item = int(X // 100)
remain = X - num_item * 100
if remain <= num_item * 5:
    print(1)
else:
    print(0)