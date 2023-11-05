import tkinter as tk
import re

class IDESimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("AESCRIPT")
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
            error_position = self.find_error_position(code)
            self.result_label.config(text=f"Código inválido en la posición: {error_position}")

    def find_error_position(self, code):
        # Expresiones regulares para encontrar errores específicos en el código
        error_patterns = [
            r"(variable\s+[a-zA-Z]+\s*=\s*[\w\.-]+;)",
            r"(funcion\s+[a-zA-Z]+\s*>>\s*{\s*[a-zA-Z]+\s*[\+\-\/*]\s*\d+\s*;\s*}\s*imprimir\(\s*[a-zA-Z]+\s*\);)",
            r"(iterar\s+\d+\s+veces\s+>>\s+[a-zA-Z]+\s*\+\s*1)",
            r"(si\s+[a-zA-Z]+\s*(>\s*|\s*<\s*)\d+\s*realiza\s*{\s*[a-zA-Z]+\s*[\+\-\/*]\s*\d+\s*;\s*}\s*)",
            r"(funcion\s+[a-zA-Z]+\s+correr\s*>>\s*{\s*>>[a-zA-Z]+\s*;\s*}\s*)"
        ]

        # Verificar cada patrón de error y encontrar la posición del error
        for pattern in error_patterns:
            match = re.search(pattern, code)
            if match is None:
                continue
            error_position = match.start()
            return error_position

        # Si no se encuentra ningún error específico, devolver la posición del primer carácter no válido
        return len(code.strip())

    def is_valid_code(self, code):
        # Expresiones regulares para validar la declaración de variables y estructuras de funciones/sentencias
        variable_pattern = r"variable\s+[a-zA-Z]+\s*=\s*[\w\.-]+;"
        function_pattern = r"funcion\s+[a-zA-Z]+\s*>>\s*{\s*[a-zA-Z]+\s*[\+\-\/*]\s*\d+\s*;\s*}\s*imprimir\(\s*[a-zA-Z]+\s*\);"
        iterar_pattern = r"iterar\s+\d+\s+veces\s+>>\s+[a-zA-Z]+\s*\+\s*1"
        si_pattern = r"si\s+[a-zA-Z]+\s*(>\s*|\s*<\s*)\d+\s*realiza\s*{\s*[a-zA-Z]+\s*[\+\-\/*]\s*\d+\s*;\s*}\s*"
        principal_pattern = r"funcion\s+[a-zA-Z]+\s+correr\s*>>\s*{\s*>>[a-zA-Z]+\s*;\s*}\s*"

        # Validar la declaración de variables, estructura de la función y sentencias
        if re.match(variable_pattern, code) or re.match(function_pattern, code) or re.match(iterar_pattern, code) or re.match(si_pattern, code) or re.match(principal_pattern, code):
            return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    ide_simulator = IDESimulator(root)
    root.mainloop()
