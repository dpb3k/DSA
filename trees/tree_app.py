import tkinter as tk
from tkinter import filedialog, messagebox
import binarytree
import AVL
import BST


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tree Visualizer")
        self.geometry("400x500")
        self.resizable(False, False)

        self.root = None
        self.avl_tree = AVL.AVLTree()

        self.bst_tree = BST.BST()

        self.label = tk.Label(self, text="Enter number of nodes for the Binary Tree:",
                              font=("Comic Sans MS", 8))
        self.label.pack(side='top', pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.build_button = tk.Button(self, text="Build Binary Tree", command=self._build_binary_tree)
        self.build_button.pack()

        self.label = tk.Label(self, text="")
        self.label.pack()

        self.label = tk.Label(self, text="Enter value for AVL Tree node:",
                              font=("Comic Sans MS", 8))
        self.label.pack(pady=10)

        self.entry2 = tk.Entry(self)
        self.entry2.pack()

        self.insert_button = tk.Button(self, text="Insert AVL Node", command=self._insert_avl_node)
        self.insert_button.pack(pady=10)

        self.build_button = tk.Button(self, text="Build AVL Tree", command=self._build_avl_tree)
        self.build_button.pack(pady=1)

        self.label = tk.Label(self, text="")
        self.label.pack()

        self.label = tk.Label(self, text="Enter value for BST Tree node:",
                              font=("Comic Sans MS", 8))
        self.label.pack(pady=10)

        self.entry3 = tk.Entry(self)
        self.entry3.pack()

        self.save_button = tk.Button(self, text="Insert BST Node", command=self._insert_bst_node)
        self.save_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Build BST Tree", command=self._build_bst_tree)
        self.save_button.pack()

        self.save_button = tk.Button(self, text="Save Tree", command=self.save_tree)
        self.save_button.pack(pady=10)

    def _build_binary_tree(self):
        try:
            num_nodes = int(self.entry.get())
            self.bt = binarytree.Trees()
            self.root = self.bt.build_binary_tree(num_nodes)
            self.bt.visualize(self.root)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of nodes.")

    def _build_avl_tree(self):
        self.root = self.avl_tree.root
        self.avl_tree.visualize(self.root)

    def _build_bst_tree(self):
        self.root = self.bst_tree.root
        self.bst_tree.visualize(self.root)

    def _insert_bst_node(self):
        try:
            value = self.entry3.get()
            self.root = self.bst_tree.insert(int(value))
            self.entry3.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def _insert_avl_node(self):
        try:
            value = self.entry2.get()
            self.root = self.avl_tree.insert(int(value))
            self.entry2.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def save_tree(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".png")
        self.bt.dot.render(filepath, view=False)


app = App()
app.mainloop()
