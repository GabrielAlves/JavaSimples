import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess
from analisdorSemanticoJavaSimples import MyVisitor as Visitor
import sys


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JavaSimples IDE")

        self.file_path = ""
        self.jasmin_path = "./jasmin.jar"
        # Menus
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New File", command=self.new_file)
        self.file_menu.add_command(label="Load File", command=self.load_file)
        self.file_menu.add_command(label="Save File", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.config_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.config_menu.add_command(label="Set Jasmin Path", command=self.set_jasmin_path)
        self.menu_bar.add_cascade(label="Config", menu=self.config_menu)

        self.root.config(menu=self.menu_bar)

        self.code_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, tabs=32, undo=True, maxundo=20)
        self.code_text.pack(fill=tk.BOTH, expand=True)
        self.code_text.edit_separator()

        # Carrega o último arquivo aberto
        self.code_text.insert('1.0', self.load_last_file())

        self.run_button = tk.Button(root, text="Compile Code", command=self.run_code)
        self.run_button.pack()

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=40, height=10,
                                                     tabs=32)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Redirecionar a saída padrão para a caixa de texto
        sys.stdout = self.OutputRedirector(self.output_text)

        # Redirecionar erros para a caixa de texto
        sys.stderr = self.ErrorRedirector(self.output_text)

    def open_terminal(self, comando):
        try:
            subprocess.Popen(["cmd.exe", "/c", comando])
        except Exception as e:
            print("Ocorreu um erro:", str(e))

    def set_jasmin_path(self):
        self.jasmin_path = filedialog.askopenfilename(filetypes=[("Jasmin files", "*.jar"), ("All files", "*.*")])

    def new_file(self):
        self.file_path = ""
        self.code_text.delete('1.0', tk.END)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'r') as file:
                self.code_text.delete('1.0', tk.END)
                self.code_text.insert('1.0', file.read())
            self.save_last_file()

    def save_file(self):
        if self.file_path == "":
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.code_text.get('1.0', tk.END))

    def load_last_file(self):
        try:
            with open('last_file.txt', 'r') as file:
                self.file_path = file.read()
                with open(self.file_path, 'r') as last_file:
                    file_data = last_file.read()
                return file_data
        except FileNotFoundError:
            return ""

    def save_last_file(self):
        with open('last_file.txt', 'w') as file:
            file.write(self.file_path)

    def run_code(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        try:
            self.save_file()
            analisador = Visitor(self.file_path)
            print("Compilando o codigo...")
            analisador.executar()
            print("Gerando Jasmin...")
            jasmin_file_path = analisador.save_jasmin_code()
            print("Criando arquivo jar...")
            comando = f"java -jar jasmin.jar {jasmin_file_path}"
            saida = subprocess.check_output(comando, shell=True, universal_newlines=True)
            print(saida)
            print("Codigo Compilado com sucesso!")
            print(f"Salvo como {jasmin_file_path[:-2]}.class")
        except Exception as e:
            result = f"{str(e)}"
            self.output_text.insert(tk.END, result)
        self.output_text.config(state=tk.DISABLED)

    class OutputRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.insert(tk.END, message)
            self.text_widget.see(tk.END)

    class ErrorRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, message, 'error')
            self.text_widget.config(state=tk.DISABLED)
            self.text_widget.see(tk.END)


if __name__ == '__main__':
    app = tk.Tk()
    gui = GUIApp(app)
    app.mainloop()
