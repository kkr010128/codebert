import math

def main():
    H = {int(input()): 1}
    ans = 0
    while True:
        new_H = {}
        for h, freq in H.items():
            ans += freq
            if h > 1:
                new_H[h // 2] = 2 * freq
        if len(new_H) == 0:
            break
        else:
            H = new_H
    print(ans)


if __name__ == '__main__':
    main()
