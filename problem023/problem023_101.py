n = int(input())

dna = set()
for i in range(n):
    command = input().split()
    if command[0] == 'insert':
        dna.add(command[1])
    else:
        print('yes' if command[1] in dna else 'no')