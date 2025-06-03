from sys import stdin


def ans():
    _in = [_.rstrip() for _ in stdin.readlines()]
    S = _in[0]  # type:str
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    if S[-1] == 's':
        S += 'es'
    else:
        S += 's'
    ans = S
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    S = list(_in[0])  # type:str
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    ans = 0
    if S[-1] == 's':
        S[-1] += 'es'
    else:
        S[-1] += 's'
    ans = ''.join(S)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)


if __name__ == "__main__":
    #main()
    ans()
