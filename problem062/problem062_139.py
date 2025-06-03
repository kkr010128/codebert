def solve(x):
    return sum([int(i) for i in str(x)])

if __name__ == '__main__':
    while True:
        x = int(input())
        if x == 0: break
        print(solve(x))