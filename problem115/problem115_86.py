a = int(input())

class calculate:
    def __init__(self,a):
        self.check = a
    
    def get_ans(self,a):
        return a + a**2 + a**3

valuable = calculate(a)

#Sprint(valuable.check)

ans = valuable.get_ans(a)

print(ans)