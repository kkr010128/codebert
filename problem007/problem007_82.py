class Fib():
    f = [1] * 50
    def fib(self, n):
        for i in range(2, n + 1):
            self.f[i] = self.f[i - 1] + self.f[i - 2]
        return(self.f[n])

x = Fib()
print(x.fib(int(input())))