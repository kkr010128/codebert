class D_Linked_List:
    class Node:
        def __init__(self, key, next = None, prev = None):
            self.next = next
            self.prev = prev
            self.key = key

    def __init__(self):
        self.nil = D_Linked_List.Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, key):
        node_x = D_Linked_List.Node(key, self.nil.next, self.nil)
        self.nil.next.prev = node_x
        self.nil.next = node_x

    def _listSearch(self, key):
        cur_node = self.nil.next
        while (cur_node != self.nil) and (cur_node.key != key):
            cur_node = cur_node.next
        return cur_node

    def _deleteNode(self, node):
        if node == self.nil:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev

    def deleteFirst(self):
        self._deleteNode(self.nil.next)

    def deleteLast(self):
        self._deleteNode(self.nil.prev)

    def deleteKey(self, key):
        node = self._listSearch(key)
        self._deleteNode(node)

    def show_keys(self):
        cur_node = self.nil.next
        keys = []
        while cur_node != self.nil:
            keys.append(cur_node.key)
            cur_node = cur_node.next
        print(' '.join(keys))


import sys

d_ll = D_Linked_List()

for i in sys.stdin:
    if 'insert' in i:
        x = i[7:-1]
        d_ll.insert(x)
    elif 'deleteFirst' in i:
        d_ll.deleteFirst()
    elif 'deleteLast' in i:
        d_ll.deleteLast()
    elif 'delete' in i:
        x = i[7:-1]
        d_ll.deleteKey(x)
    else:
        pass

d_ll.show_keys()