import tkinter as tk
from tkinter import filedialog, Text

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("My Daily Planner")

        self.text_area = Text(root)
        self.text_area.pack(expand=1, fill='both')

        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)  # New "Open" command
        file_menu.add_command(label="Save", command=self.save_file)

        self.filepath = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filepath = None

    def open_file(self):  # New "Open" method
        self.filepath = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not self.filepath:
            return
        with open(self.filepath, 'r') as file:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if self.filepath is None:
            self.filepath = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
        if not self.filepath:
            return
        with open(self.filepath, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
