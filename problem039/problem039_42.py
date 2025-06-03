def judge(a, b, c):
    return 'Yes' if a < b < c else 'No'

if __name__ == '__main__':
    a, b, c = map(int, input().split(' '))
    print(judge(a, b, c))

