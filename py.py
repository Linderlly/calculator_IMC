import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")
        
        if imc < 18.5:
            messagebox.showinfo("Resultado", f"""Seu IMC é: {imc:.2f} 
Você está abaixo do peso.""")
        elif 18.5 <= imc < 24.9:
            messagebox.showinfo("Resultado", f"""Seu IMC é: {imc:.2f} 
Você está com peso normal.""")
        elif 25 <= imc < 29.9:
            messagebox.showinfo("Resultado", f"""Seu IMC é: {imc:.2f} 
Você está com sobrepeso.""")
        else:
            messagebox.showinfo("Resultado", f"""Seu IMC é: {imc:.2f} 
Você está com obesidade.""")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")


root = tk.Tk()
root.title("Calculadora de IMC")


label_peso = tk.Label(root, text="Peso (kg):")
label_peso.pack()

entry_peso = tk.Entry(root)
entry_peso.pack()

label_altura = tk.Label(root, text="Altura (m):")
label_altura.pack()

entry_altura = tk.Entry(root)
entry_altura.pack()

button_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
button_calcular.pack()

label_resultado = tk.Label(root, text="Seu IMC será mostrado aqui.")
label_resultado.pack()


root.mainloop()
