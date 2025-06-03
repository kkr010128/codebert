def main():
    N = int(input())
    S = str(input())
    ans = ''
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(S)):
        c = alphabet.index(S[i]) + N
        if c > 25:
            c = c - 26
        ans = ans + alphabet[c]
    print(ans)
main()