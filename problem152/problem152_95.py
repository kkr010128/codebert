import sys
def input(): return sys.stdin.readline().strip()
mod = 998244353


def main():

    """
    各トークンを(最下点、最終的な高さ)に分けるのはできた。
    そしてそれらを最下点位置が浅い順に並べるのも悪くはなかった、増加パートに関しては。

    減少パートは減少度合が小さい順に付け加えたとしても高さが負に潜り込むケースがある。
    （例）高さ3から下るとして、(-1, -1), (-2, 0), (-3, -2)が各トークンとすると
        この順にくっつけると(-3, -2)を加えるときにアウトだが、
        (-2, 0), (-3, -2), (-1, -1)の順だったらOK
    
    なので下る場合には増加パートとは違う方法でくっつけないといけない。
    結論としては、これは左右反転させれば増加していることになるので、右からくっつけるようにすればいい。
    """

    N = int(input())
    S_up = []
    S_down = []
    for _ in range(N):
        s = input()
        max_depth = 0
        height = 0
        for c in s:
            if c == '(':
                height += 1
            else:
                height -= 1
                max_depth = min(max_depth, height)
        if height > 0: S_up.append((max_depth, height - max_depth))
        else: S_down.append((-(height - max_depth), -max_depth))
    S_up.sort(key=lambda x: (x[0], x[1]))
    S_down.sort(key=lambda x: (x[0], x[1]))

    height_left = 0
    while S_up:
        d, h = S_up.pop()
        #print("({}, {})".format(d, h))
        if height_left + d < 0:
            print("No")
            return
        height_left += d+h

    height_right = 0
    while S_down:
        d, h = S_down.pop()
        #print("({}, {})".format(d, h))
        if height_right + d < 0:
            print("No")
            return
        height_right += d+h

    if height_left != height_right: print("No")
    else: print("Yes")





if __name__ == "__main__":
    main()
