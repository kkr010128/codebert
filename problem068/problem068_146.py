# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_D

def reverse(s, a, b):
    s1 = s[0:a]
    s2 = s[a:b+1]
    s2 = s2[::-1]
    s3 = s[b+1:len(string)]
    return s1 + s2 + s3
def replace(s, a, b, p):
    s1 = s[0:a]
    s2 = p
    s3 = s[b+1:len(string)]
    return s1 + s2 + s3

string = input()
q = int(input())

for _ in range(q):
    c = input().split()

    if c[0] == "print":
        print(string[int(c[1]):int(c[2])+1])
    if c[0] == "reverse":
        string = reverse(string, int(c[1]), int(c[2]))
    if c[0] == "replace":
        string = replace(string, int(c[1]), int(c[2]), c[3])