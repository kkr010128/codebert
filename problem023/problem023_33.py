n = int(input())
d = set()
for _ in range(n):
    command = input()
    if 'i' == command[0]:
        _, word = command.split()
        d.add(word)
    else:
        _, word = command.split()
        print('yes' if word in d else 'no')