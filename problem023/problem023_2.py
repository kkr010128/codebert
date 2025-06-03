import sys

def main():
    lines = sys.stdin.readlines()
    n = int(lines[0])

    repo = {}
    for i in range(1, n + 1):
        command, acgt = lines[i].split()
        if command[0] == 'i':
            if acgt not in repo:
                repo[acgt] = 0
        elif command[0] == 'f':
            if acgt in repo:
                print('yes')
            else:
                print('no')
    return


main()
