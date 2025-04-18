import json
import os
import tkinter as tk
from tkinter import messagebox

# Nome do arquivo
filename = "letters_data.json"

# Carrega os dados do arquivo, se existir
if os.path.exists(filename):
    with open(filename, "r") as file:
        how_much_i_did = json.load(file)
else:
    how_much_i_did = []

# Função para adicionar número
def add_number():
    try:
        number = int(entry.get())
        how_much_i_did.append(number)
        entry.delete(0, tk.END)

        # Salva no arquivo
        with open(filename, "w") as file:
            json.dump(how_much_i_did, file)

        messagebox.showinfo("Adicionado!", f"{number} cartas adicionadas.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")

# Função para mostrar total
def show_total():
    total = sum(how_much_i_did)
    messagebox.showinfo("Total de cartas", f"Você escreveu {total} cartas no total.")

# Criando a interface
root = tk.Tk()
root.title("Contador de Cartas")

# Layout
label = tk.Label(root, text="Quantas cartas você escreveu agora?")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_add = tk.Button(root, text="Adicionar", command=add_number)
btn_add.pack(pady=5)

btn_total = tk.Button(root, text="Ver total", command=show_total)
btn_total.pack(pady=10)

# Rodar o app
root.mainloop()
