import tkinter as tk
from arbol import insert

class AVLTreeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("AVL Tree Visualization")
        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()
        self.root = None

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.insert_button = tk.Button(master, text="Insert", command=self.insert_key)
        self.insert_button.pack()

    def insert_key(self):
        key = int(self.entry.get())
        self.root = insert(self.root, key)
        self.canvas.delete("all")
        self.draw_tree(self.root, 300, 20, 100)

    def draw_tree(self, node, x, y, dx):
        if node:
            self.canvas.create_text(x, y, text=str(node.key), font=("Arial", 12))
            if node.left:
                self.canvas.create_line(x, y, x - dx, y + 50)
                self.draw_tree(node.left, x - dx, y + 50, dx // 2)
            if node.right:
                self.canvas.create_line(x, y, x + dx, y + 50)
                self.draw_tree(node.right, x + dx, y + 50, dx // 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = AVLTreeGUI(root)
    root.mainloop()
