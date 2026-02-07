a = [[1, 2, 3]]*10
print(a)
a[0][0] = 100
print(a)


class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = self
            self.prev = self

    def __init__(self):
        self.sentinel = self.Node('служебная вершина')

    def link(self, n1, n2):
        n1.next = n2
        n2.prev = n1

    def unlink(self, n1):
        pr = n1.prev
        nx = n1.next
        pr.next = nx
        nx.prev = pr
        n1.prev = n1
        n1.next = n1

    def insert(self, new_node, position_node):
        next_node = position_node.next
        self.link(position_node, new_node)
        self.link(new_node, next_node)

    