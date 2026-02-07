# Реализовать класс бинарного дерева. Написать функцию для нахождения наибольшей 
# глубины листьев в бинарном дереве.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Вставка как в бинарное дерево поиска
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)

    def max_depth(self):
        # Вызывает рекурсивную функцию для корня
        return self._max_depth(self.root)

    def _max_depth(self, node):
        if node is None:
            return 0
        left_depth = self._max_depth(node.left)
        right_depth = self._max_depth(node.right)
        return max(left_depth, right_depth) + 1
