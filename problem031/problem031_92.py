import statistics
while True:
    num = input()
    if num == '0':
        break
    value = map(int, input().split())
    print(statistics.pstdev(value))
