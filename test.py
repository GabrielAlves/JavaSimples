import tkinter as tk
import sys
from tkinter import scrolledtext
from io import StringIO


class TerminalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal App")

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.redirect_output()

    def redirect_output(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

        sys.stdout = self.TextRedirector(self.text_area, "stdout")
        sys.stderr = self.TextRedirector(self.text_area, "stderr")

    class TextRedirector:
        def __init__(self, text_widget, tag):
            self.text_widget = text_widget
            self.tag = tag

        def write(self, message):
            self.text_widget.insert(tk.END, message, (self.tag,))
            self.text_widget.see(tk.END)  # Scroll to the end of the text
            self.text_widget.update()  # Update the widget to display the new message

    def restore_output(self):
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr


if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalApp(root)
    root.mainloop()
    app.restore_output()  # Restore the original output streams when the app exits
