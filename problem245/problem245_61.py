def main():
    N = int(input())
    S = input()

    ans = 0
    for i in range(len(S) - 1):
        if S[i:i + 3] == 'ABC':
            ans += 1
    print(ans)
    

main()