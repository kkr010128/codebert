letters = input()
q = int(input())
for _ in range(q):
    words = input().split()
    command = words[0]
    a, b = map(int, words[1:3])

    if command == 'replace':
        letters = ''.join([letters[:a], words[3], letters[b+1:]])
    elif command == 'reverse':
        letters = ''.join([letters[:a ], letters[a:b+1][::-1], letters[b+1:]])
    elif command == 'print':
        print(letters[a:b+1])
        
