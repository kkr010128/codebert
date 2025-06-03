from sys import stdin, stdout

int_in = lambda: int(stdin.readline())
arr_in = lambda: [int(x) for x in stdin.readline().split()]
mat_in = lambda rows: [arr_in() for y in range(rows)]
str_in = lambda: stdin.readline().strip()
out = lambda o: stdout.write("{}\n".format(o))
arr_out = lambda o: out(" ".join(map(str, o)))
bool_out = lambda o: out("YES" if o else "NO")
tests = lambda: range(1, int_in() + 1)
case_out = lambda i, o: out("Case #{}: {}".format(i, o))


def solve(h1, m1, h2, m2, k):
    sleep_at = h2 * 60 + m2
    wake_at = h1 * 60 + m1
    return sleep_at - wake_at - k


if __name__ == "__main__":
    h1, m1, h2, m2, k = arr_in()
    out(solve(h1, m1, h2, m2, k))