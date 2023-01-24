import graphviz


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data)
            self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.data)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data)

    def visualize(self, root):
        dot = graphviz.Digraph()
        self._visit(root, dot)
        dot.attr(size='60,50')
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

