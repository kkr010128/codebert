my_set = set()

n = int(input())
for _ in range(n):
    command, dna = input().split()
    if command == 'insert':
        my_set.add(dna)
    elif dna in my_set:
        print('yes')
    else:
        print('no')
