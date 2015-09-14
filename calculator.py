import tkinter as tk
memo = {}

class Calculator:
    def __init__(self, master):

        self.display_var = tk.StringVar(master)
        tk.Label(master, textvariable=self.display_var).grid(column=3)
        self.display_var.set('0')

        tk.Button(master, text='7', command=self.seven_button).grid(row=1)
        tk.Button(master, text='8', command=self.eight_button).grid(row=1, column=1)
        tk.Button(master, text='9', command=self.nine_button).grid(row=1, column=2)
        tk.Button(master, text='+', command=self.plus_button).grid(row=1, column=3)
        tk.Button(master, text='4', command=self.four_button).grid(row=2)
        tk.Button(master, text='5', command=self.five_button).grid(row=2, column=1)
        tk.Button(master, text='6', command=self.six_button).grid(row=2, column=2)

    def one_button(self):
        pass
    def two_button(self):
        pass
    def three_button(self):
        pass
    def four_button(self):
        pass
    def five_button(self):
        pass
    def six_button(self):
        pass
    def seven_button(self):
        pass
    def eight_button(self):
        pass
    def nine_button(self):
        pass
    def plus_button(self):
        pass
    def minus_button(self):
        pass
    def multiply_button(self):
        pass
    def divide_button(self):
        pass
    def enter_button(self):
        pass
    def clear_button(self):
        pass
    def clearall_button(self):
        pass
    def signchange_button(self):
        pass
    def undo_button(self):
        pass
def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.title('Calculator')
    root.mainloop()

if __name__ == '__main__':
    main()
