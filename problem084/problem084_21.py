from networkx import *
print(max(*map(len,connected_components(Graph([*map(str.split,open(0))][1:]))),1,0))