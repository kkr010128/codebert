def main(S, T):
    ans = len(T)
    for w in range(len(S)-len(T)+1):
        tmp = len(T)
        for s, t in zip(S[w:w+len(T)], T):
            if s == t:
                tmp -= 1
        if tmp < ans:
            ans = tmp
    return ans

if __name__ == '__main__':
    S = input()
    T = input()
    ans = main(S, T)
    print(ans)

