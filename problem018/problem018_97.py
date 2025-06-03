
Stack=[]
def push(x):
    Stack.append(x)

def pop():
    return Stack.pop()

def solve():
    s_list=raw_input().split()
    for i in range(len(s_list)):
        if s_list[i]=='+':
            b=pop()
            a=pop()
            push(a+b)
        elif s_list[i]=='-':
            b=pop()
            a=pop()
            push(a-b)
        elif s_list[i]=='*':
            b=pop()
            a=pop()
            push(a*b)
        else:
            push(int(s_list[i]))
    print(pop())

def main():
    if __name__=="__main__":
        solve()

main()