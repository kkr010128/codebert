#
# author Sidratul
#

if __name__ == '__main__':
    n = list(input())
    n = sum([int(i) for i in n])
    if n % 9 == 0:
        print('Yes')
    else:
        print('No')