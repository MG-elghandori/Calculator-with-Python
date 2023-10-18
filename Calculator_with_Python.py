import tkinter as tk
from tkinter import ttk

class Calculatrice:
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.title("Calculatrice")
        self.gui.configure(background="#101419")
        self.gui.geometry("340x210")
        self.equation = tk.StringVar()
        self.equation.set("0")

      
        self.button_style = ttk.Style()
        self.button_style.configure('TButton', background='#476C9B')


        self.label_style = ttk.Style()
        self.label_style.configure('TLabel', background='blue', foreground='#FFFFFF', font=('Helvetica', 18))

        self.result = ttk.Label(self.gui, textvariable=self.equation, width=25, style='TLabel')
        self.result.grid(columnspan=4)

        boutons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '=',
            'C'
        ]
        row = 1
        col = 0
        for bouton in boutons:
            b = ttk.Button(self.gui, text=str(bouton), command=lambda b=bouton: self.cliquer(b), style='TButton')
            b.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 4:
                col = 0
                row += 1

    def cliquer(self, bouton):
        if bouton == '=':
            try:
                self.equation.set(eval(self.equation.get()))
            except:
                self.equation.set("Erreur")
        elif bouton == 'C':
            self.equation.set("0")
        else:
            if self.equation.get() == "0" or self.bouton_clic == '=':
                self.equation.set(bouton)
            else:
                self.equation.set(self.equation.get() + bouton)
        self.bouton_clic = bouton

    def run(self):
        self.gui.mainloop()

# run the calculator
calc = Calculatrice()
calc.run()
