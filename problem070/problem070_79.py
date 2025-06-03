code = """

# distutils: language=c++
# distutils: include_dirs=[/home/USERNAME/.local/lib/python3.8/site-packages/numpy/core/include, /opt/ac-library]
# cython: boundscheck=False
# cython: wraparound=False

from libcpp cimport bool
from libc.stdio cimport getchar, printf
from libcpp.string cimport string
from libcpp.vector cimport vector
cdef extern from "<atcoder/dsu>" namespace "atcoder":
    cdef cppclass dsu:
        dsu(int n)
        int merge(int a, int b)
        bool same(int a, int b)
        int leader(int a)
        int size(int a)
        vector[vector[int]] groups()

cdef class Dsu:
    cdef dsu *_thisptr
    def __cinit__(self, int n):
        self._thisptr = new dsu(n)
    cpdef int merge(self, int a, int b):
        return self._thisptr.merge(a, b)
    cpdef bool same(self, int a, int b):
        return self._thisptr.same(a, b)
    cpdef int leader(self, int a):
        return self._thisptr.leader(a)
    cpdef int size(self, int a):
        return self._thisptr.size(a)
    cpdef vector[vector[int]] groups(self):
        return self._thisptr.groups()

cpdef inline vector[int] ReadInt(int n):
    cdef int b, c
    cdef vector[int] *v = new vector[int]()
    for i in range(n):
        c = 0
        while 1:
            b = getchar() - 48
            if b < 0: break
            c = c * 10 + b
        v.push_back(c)
    return v[0]

cpdef inline vector[string] Read(int n):
    cdef char c
    cdef vector[string] *vs = new vector[string]()
    cdef string *s
    for i in range(n):
        s = new string()
        while 1:
            c = getchar()
            if c<=32: break
            s.push_back(c)
        vs.push_back(s[0])
    return vs[0]

cpdef inline void PrintLongN(vector[long] l):
    cdef int n = l.size()
    for i in range(n): printf("%ld\\n", l[i])

cpdef inline void PrintLong(vector[long] l):
    cdef int n = l.size()
    for i in range(n): printf("%ld ", l[i])
"""


import os, sys, getpass

if sys.argv[-1] == 'ONLINE_JUDGE':
    code = code.replace("USERNAME", getpass.getuser())
    open('atcoder.pyx','w').write(code)
    os.system('cythonize -i -3 -b atcoder.pyx')
    sys.exit(0)


from atcoder import Dsu, ReadInt

def main():
    N,M = ReadInt(2)
    dsu = Dsu(N)
    for i in range(M):
        a,b = ReadInt(2)
        dsu.merge(a-1,b-1)
    print(len(dsu.groups())-1)

if __name__ == "__main__":
    main()