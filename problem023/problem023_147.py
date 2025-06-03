dict = {}

def insert(word):
    global dict

    dict[word] = 0

def find(word):
    global dict
    if word in dict:
        print('yes')
    else:
        print('no')

def main():
    N = int(input())
    order = [list(input().split()) for _ in range(N)]

    for i in range(N):
        if order[i][0] == 'insert':
            insert(order[i][1])
        elif order[i][0] == 'find':
            find(order[i][1])

main()

