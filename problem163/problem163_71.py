import copy

def main():
    h, o = map(int, input().split(' '))
    if h <= o:
        print('unsafe')
    else:
        print('safe')
main()