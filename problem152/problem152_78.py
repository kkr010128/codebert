from collections import namedtuple
Line = namedtuple('Line', ['lowest', 'end'])


def main():
    N = int(input())
    up_lines = []
    down_lines = []
    for i in range(N):
        s = input()
        now = 0
        lowest = 0
        for c in s:
            if c == "(":
                now += 1
            else:
                now -= 1
                lowest = min(lowest, now)
        if now > 0:
            up_lines.append(Line(lowest, now))
        else:
            down_lines.append(Line(lowest-now, -now))
    up_lines.sort(key=lambda line: -line.lowest)
    down_lines.sort(key=lambda line: -line.lowest)
    left = 0
    for line in up_lines:
        if left + line.lowest < 0:
            print("No")
            return
        left += line.end
        if left < 0:
            print("No")
            break
    right = 0
    for line in down_lines:
        if right + line.lowest < 0:
            print("No")
            return
        right += line.end
        if right < 0:
            print("No")
            break
    if left == right:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
