class Solution:

    def solve(self, N: int, P: int, S: str):

        if P == 2 or P == 5:
            answer = 0
            for idx, s in enumerate(S):
                if int(s) % P == 0:
                    answer += idx + 1

        else:
            answer = 0
            U = [0] * P  # int(S[i,N] mod P
            U[0] += 1

            num = 0
            base10_mod_p = 1
            for i in range(N):
                num = (num + int(S[N-i-1]) * base10_mod_p) % P
                base10_mod_p = (base10_mod_p * 10) % P

                U[num] += 1

            for u in U:
                answer += u * (u-1) // 2

        return answer


if __name__ == '__main__':

    # standard input
    N, P = map(int, input().split())
    S = input()

    # solve
    solution = Solution()
    answer = solution.solve(N, P, S)
    print(answer)
