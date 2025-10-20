import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Calculadora de Divisão")

label_num1 = tk.Label(janela, text="Dividendo:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Divisor:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

def div_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"O Quociente é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")

botao_dividir = tk.Button(janela, text="Dividir", command=div_numeros)
botao_dividir.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    janela.mainloop()