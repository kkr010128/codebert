n=int(input());a=list(map(int,input().split()));dict={i+1:a[i] for i in range(n)}
print(*[i[0] for i in sorted(dict.items(),key=lambda x:x[1])],sep=' ')