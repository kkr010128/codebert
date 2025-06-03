#B
N, A, B=map(int, input().split())

quotient=N//(A+B)
remainder=N%(A+B)
quo_bball=quotient*A
if remainder <=A:
    rem_bball=remainder
else:
    rem_bball=A
print(quo_bball+rem_bball)