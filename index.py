import tkinter as tk
import re

class IDESimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("IDE Simulator")
        self.text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=50)
        self.text_widget.pack(expand=tk.YES, fill=tk.BOTH)
        self.validation_button = tk.Button(root, text="Validar", command=self.validate_code)
        self.validation_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def validate_code(self):
        code = self.text_widget.get("1.0", tk.END)
        if self.is_valid_code(code):
            self.result_label.config(text="Código válido")
        else:
            self.result_label.config(text="Código inválido")

    def is_valid_code(self, code):
        # Expresión regular para validar la declaración de variables con números (positivos y negativos) hasta 1000000
        variable_pattern = r"variable\s+[a-zA-Z]+\s*=\s*-?\d+;"
        
        # Expresión regular para validar la estructura de la función y la palabra reservada "imprimir"
        function_pattern = r"funcion\s+[a-zA-Z]+\s*>>\s*{\s*[a-zA-Z]+\s*[\+\-\/*]\s*\d+\s*;\s*}\s*imprimir\(\s*[a-zA-Z]+\s*\);"
        
        # Validar la declaración de variables y la estructura de la función y la palabra reservada "imprimir"
        if re.match(variable_pattern, code) or re.match(function_pattern, code):
            return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    ide_simulator = IDESimulator(root)
    root.mainloop()
