import sys, math, operator, itertools, collections, heapq, bisect
# sys.setrecursionlimit(10**4)


class Solution:
    def __init__(self):
        pass

    def solve(self, *Input):
        ans = 0
        h,w,k,matrix = Input
        # print(matrix)
        for r in range(h):
            rows = list(itertools.combinations(range(h),r))
            for c in range(w):
                # print(r,c)
                cols = list(itertools.combinations(range(w), c))
                # print(list(rows), list(cols))
                for row in rows:
                    for col in cols:
                        # print(row,col)
                        new_matrix = [[x for x in ROW] for ROW in matrix]
                        ans += self.create(h,w,k,new_matrix,row,col)
                        # print(ans)

        return ans

    def create(self, *Input):
        h,w,k,matrix,rows,cols = Input
        for i in range(h):
            for j in cols:
                matrix[i][j] = '.'
        for r in rows:
            matrix[r] = ['.'] * w
        # print(matrix)
        return self.check(k,matrix)

    def check(self, *Input):
        k,matrix = Input
        cnt = 0
        for row in matrix:
            cnt += row.count('#')
        return cnt == k

    def sieve_classic(self,a,b):
        self.primes = [True] * (b+1)
        self.primes[0] = self.primes[1] = False
        for i in range(2,b+1):
            if self.primes[i] and i*i <= b:
                for j in range(i*i,b+1,i):
                    self.primes[j] = False
        self.primes = [x for x,y in enumerate(self.primes) if y]
        ind = bisect.bisect_left(self.primes,a)
        self.primes[:ind] = []
        return None


if __name__=='__main__':
    solution = Solution()

    inputs = iter(sys.stdin.readlines())
    h,w,k = map(int, next(inputs).split())
    matrix = [list(next(inputs).rstrip()) for _ in range(h)]
    ans = solution.solve(h,w,k,matrix)
    print(ans)
