import random

import graphviz


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class Trees:
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

    def build_binary_tree(self, num_nodes):
        if num_nodes == 0:
            return None
        root = Node(1)
        nodes = [root]
        for i in range(2, num_nodes + 1):
            parent = random.choice(nodes)
            if parent.left is None:
                parent.left = Node(i)
                nodes.append(parent.left)
            elif parent.right is None:
                parent.right = Node(i)
                nodes.append(parent.right)
        return root




