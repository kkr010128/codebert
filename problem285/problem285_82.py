from sys import stdin, stdout

int_in = lambda: int(stdin.readline())
arr_in = lambda: [int(x) for x in stdin.readline().split()]
mat_in = lambda rows: [arr_in() for y in range(rows)]
str_in = lambda: stdin.readline().strip()
out = lambda o: stdout.write("{}\n".format(o))
arr_out = lambda o: out(" ".join(map(str, o)))
bool_out = lambda o: out("YES" if o else "NO")
tests = lambda: range(1, int_in() + 1)


def solve(s):
    start_up = s[0] == "<"
    curr_up = start_up
    counts = [1]
    for c in s[1:]:
        if curr_up == (c == "<"):
            counts[-1] += 1
        else:
            curr_up = not curr_up
            counts.append(1)

    curr_up = start_up
    result = counts[0]*(counts[0]-1)//2
    if not curr_up:
        result += counts[0]
    for i in range(1, len(counts)):
        if curr_up:
            result += max(counts[i-1], counts[i])
        result += counts[i]*(counts[i]-1)//2
        curr_up = not curr_up
    if curr_up:
        result += counts[-1]

    return result


if __name__ == "__main__":
    s = str_in()
    out(solve(s))