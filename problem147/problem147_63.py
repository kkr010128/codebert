def main(S, T):
    if len(S)+1 == len(T) and S == T[:-1]:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    S = input()
    T = input()
    ans = main(S, T)
    print(ans)

