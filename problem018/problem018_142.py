#coding:UTF-8
def Stack(A):
    p=[]
    symbol=["+","-","*"]
    for i in range(len(A)):
        if A[i] in symbol:
            if A[i]=="+":
                p.append(p.pop()+p.pop())
            elif A[i]=="-":
                p.append(-p.pop()+p.pop())
            else:
                p.append(p.pop()*p.pop())
        else:
            p.append(int(A[i]))
    
    print(p[0])
  
if __name__=="__main__":
    a=input()
    A=a.split(" ")
    Stack(A)