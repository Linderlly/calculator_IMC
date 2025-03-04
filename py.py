import tkinter as tk
from tkinter import ttk, messagebox

def calcular_imc(event=None):
    try:
        peso_texto = entry_peso.get().strip()
        altura_texto = entry_altura.get().strip()

        if not peso_texto or not altura_texto:
            mensagem_erro = "Por favor, preencha todos os campos:\n"
            if not peso_texto:
                mensagem_erro += "- Peso (kg)\n"
            if not altura_texto:
                mensagem_erro += "- Altura (m)"
            messagebox.showerror("Erro", mensagem_erro)
            return

        peso = float(peso_texto)
        altura = float(altura_texto)
        imc = peso / (altura ** 2)
        resultado_texto = f"Seu IMC é: {imc:.2f}"
        label_resultado.config(text=resultado_texto)

        if imc < 18.5:
            status = "Você está abaixo do peso."
            cor = "#FFCC00"
        elif 18.5 <= imc < 24.9:
            status = "Você está com peso normal."
            cor = "#00CC66"
        elif 25 <= imc < 29.9:
            status = "Você está com sobrepeso."
            cor = "#FF6600"
        else:
            status = "Você está com obesidade."
            cor = "#CC0000"

        label_resultado.config(foreground=cor)
        messagebox.showinfo("Resultado", f"{resultado_texto}\n{status}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")

def limpar_campos():
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    label_resultado.config(text="Seu IMC será mostrado aqui.", foreground="black")

root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

frame = ttk.Frame(root, padding="15", relief="ridge", borderwidth=5)
frame.pack(expand=True, fill="both")

label_titulo = ttk.Label(frame, text="Calculadora de IMC", font=("Arial", 14, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

label_peso = ttk.Label(frame, text="Peso (kg):", font=("Arial", 11))
label_peso.grid(row=1, column=0, padx=5, pady=5, sticky="W")
entry_peso = ttk.Entry(frame, font=("Arial", 11))
entry_peso.grid(row=1, column=1, padx=5, pady=5)

label_altura = ttk.Label(frame, text="Altura (m):", font=("Arial", 11))
label_altura.grid(row=2, column=0, padx=5, pady=5, sticky="W")
entry_altura = ttk.Entry(frame, font=("Arial", 11))
entry_altura.grid(row=2, column=1, padx=5, pady=5)

button_calcular = ttk.Button(frame, text="Calcular IMC", command=calcular_imc)
button_calcular.grid(row=3, column=0, columnspan=2, pady=10, ipadx=10)

button_limpar = ttk.Button(frame, text="Limpar", command=limpar_campos)
button_limpar.grid(row=4, column=0, columnspan=2, pady=5, ipadx=10)

label_resultado = ttk.Label(frame, text="Seu IMC será mostrado aqui.", font=("Arial", 12, "bold"), anchor="center")
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

root.bind('<Return>', calcular_imc)

root.mainloop()
