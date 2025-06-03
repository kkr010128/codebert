"""
AtCoder :: Beginner Contest 175 :: C - Walking Takahashi 
https://atcoder.jp/contests/abc175/tasks/abc175_c
"""
import sys


def solve(X, K, D):
    """Solve puzzle."""
    # print('solve X', X, 'K', K, 'D', D)
    if D == 0:
        return X

    X = abs(X)
    soln = abs(X - (K * D))
    steps_to_zero = abs(X) // D
    # print('steps to zero', steps_to_zero, K - steps_to_zero)
    # print('to zero', abs(X - (steps_to_zero * D)))
    # Undershoot or get directly on to zero.
    if steps_to_zero <= K and ((K - steps_to_zero) % 2 == 0):
        soln = min(soln, abs(X - (steps_to_zero * D)))

    # Overshoot by one step
    steps_past_zero = steps_to_zero + 1
    # print('steps past zero', steps_past_zero, K - steps_past_zero)
    # print('past zero', abs(X - (steps_past_zero * D))) 
    if steps_past_zero <= K and ((K - steps_past_zero) % 2 == 0):
        soln = min(soln, abs(X - (steps_past_zero * D)))

    # Overshoot and return by one
    steps_back_zero = steps_past_zero + 1
    # print('steps back zero', steps_back_zero, K - steps_back_zero)
    # print('back zero', abs(X - (steps_back_zero * D)))
    if steps_back_zero <= K and ((K - steps_back_zero) % 2 == 0):
        soln = min(soln, abs(X - (steps_back_zero * D)))

    return soln


def main():
    """Main program."""
    X, K, D = (int(i) for i in sys.stdin.readline().split())
    print(solve(X, K, D))


if __name__ == '__main__':
    main()
