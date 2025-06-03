def shuffle(index):
    global a
    a = a[index:]+a[:index]
    
while True:
    a = input()
    if a == '-':
        break
    for i in range(int(input())):
        shuffle(int(input()))
    print(a)