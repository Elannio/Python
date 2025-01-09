import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("300x350")
        
        self.result_var = tk.StringVar()
        
        self.entry = tk.Entry(self.master, textvariable=self.result_var, justify='right', width=45)
        self.entry.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 2, 0), ('9', 3, 0),
            ('4', 1, 1), ('5', 2, 1), ('6', 3, 1),
            ('1', 1, 2), ('2', 2, 2), ('3', 3, 2),
            ('0', 2, 3), ('=', 4, 3), (',', 3, 3),
            ('+', 4, 2), ('-', 4, 1), ('*', 4, 0),
            ('C', 1, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(self.master, text=text, font=("Arial", 14), width=5, height=2, command=self.evaluate)
            elif text == 'C':
                button = tk.Button(self.master, text=text, font=("Arial", 14), width=5, height=2, command=self.clear)
            else:
                button = tk.Button(self.master, text=text, font=("Arial", 14), width=5, height=2, command=lambda t=text: self.append_text(t))
                
            button.grid(row=row, column=col, padx=5, pady=5)
            
    def append_text(self, text):
        current_text = self.result_var.get()
        self.result_var.set(current_text + text)
        
    def evaluate(self):
        try: 
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")
            
    def clear(self):
        self.result_var.set("") 
        
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()