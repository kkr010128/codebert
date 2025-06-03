code = r"""
# distutils: language=c++
# distutils: include_dirs=/opt/ac-library
from libcpp cimport bool
from libcpp.vector cimport vector
cdef extern from "<atcoder/dsu>" namespace "atcoder":
    cdef cppclass dsu:
        dsu(int n)
        int merge(int a, int b)
        bool same(int a, int b)
        int leader(int a)
        int size(int a)
        vector[vector[int]] groups()
from libc.stdio cimport getchar, printf
cdef inline int read() nogil:
    cdef int b, c = 0
    while 1:
        b = getchar() - 48
        if b < 0: return c
        c = c * 10 + b
cdef int n = read(), i
cdef dsu *u = new dsu(n)
for i in range(read()): u.merge(read() - 1, read() - 1)
printf('%lu\n', u.groups().size() - 1)
"""
import os, sys
if sys.argv[-1] == 'ONLINE_JUDGE':
    open('solve.pyx', 'w').write(code)
    os.system('cythonize -i -3 -b solve.pyx')
import solve