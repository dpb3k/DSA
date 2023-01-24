import graphviz


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(key, self.root)
        return self.root

    def _insert(self, key, root):
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self._insert(key, root.left)
        else:
            root.right = self._insert(key, root.right)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def visualize(self, root):
        dot = graphviz.Digraph()
        self._visit(root, dot)
        dot.attr(size='40,40')
        dot.attr(seed='1')
        dot.render(view=True, format='png', engine='dot')

    def _visit(self, node, dot):
        if node:
            dot.node(str(node.data))
            if node.left:
                dot.edge(str(node.data), str(node.left.data))
                self._visit(node.left, dot)
            if node.right:
                dot.edge(str(node.data), str(node.right.data))
                self._visit(node.right, dot)

