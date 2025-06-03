import os
import heapq
import sys
import math
import operator
from collections import defaultdict
from io import BytesIO, IOBase


"""def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)"""

"""def pw(a,b):
    result=1
    while(b>0):
        if(b%2==1): result*=a
        a*=a
        b//=2
    return result"""



def inpt():
    return [int(k) for k in input().split()]

def check(mid,k,ar):
    ct=k
    for i in ar:
        if(i<=mid):
            continue
        ct-=(i//mid)
    return ct>=0
def main():
    n,k=map(int,input().split())
    ar=inpt()
    i,j=1,100000000000
    while(i<j):
        mid=(i+j)//2
        if(check(mid,k,ar)):
            j=mid
        else:
            i=mid+1
    print(i)

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()
