def main():
    a, b, c = map(int, input().split())
    if 21 < (a + b + c):
        print('bust')
    else:
        print('win')
    
main()