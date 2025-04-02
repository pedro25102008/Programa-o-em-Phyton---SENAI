import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def conectar():
    return sqlite3.connect('comercio.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    # Criar a tabela de clientes
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo cliente
def inserir_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO clientes(nome, email, telefone, endereco) VALUES(?, ?, ?, ?)', 
                  (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'Cliente cadastrado com sucesso!')
        mostrar_clientes()
    else:
        messagebox.showerror('ERRO', 'Preencha todos os campos obrigatórios.')

# Função para listar os clientes cadastrados
def mostrar_clientes():
    for row in tree.get_children():
        tree.delete(row)
    
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    clientes = c.fetchall()
    
    for cliente in clientes:
        tree.insert("", "end", values=(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))
    
    conn.close()

# Função para excluir um cliente
def delete_cliente():
    dado_del = tree.selection()
    if dado_del:
        cliente_id = tree.item(dado_del)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'Cliente excluído com sucesso!')
        mostrar_clientes()
    else:
        messagebox.showerror('ERRO', 'Selecione um cliente para excluir.')

# Função para editar os dados de um cliente
def editar_cliente():
    selecao = tree.selection()
    if selecao:
        cliente_id = tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()
        novo_email = entry_email.get()
        novo_telefone = entry_telefone.get()
        novo_endereco = entry_endereco.get()

        if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE clientes SET nome = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?', 
                      (novo_nome, novo_email, novo_telefone, novo_endereco, cliente_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('AVISO', 'Dados do cliente atualizados com sucesso!')
            mostrar_clientes()
        else:
            messagebox.showwarning('AVISO', 'Preencha todos os campos obrigatórios.')
    else:
        messagebox.showerror('ERRO', 'Selecione um cliente para editar.')

# Interface Gráfica

janela = tk.Tk()
janela.title('Cadastro de Clientes - Comércio XYZ')

# LabelFrame para o formulário de cadastro
frame_cliente = tk.LabelFrame(janela, text="Cadastro de Cliente", padx=10, pady=10)
frame_cliente.grid(row=0, column=0, padx=10, pady=10)

label_nome = tk.Label(frame_cliente, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(frame_cliente)
entry_nome.grid(row=0, column=1)

label_email = tk.Label(frame_cliente, text="E-mail:")
label_email.grid(row=1, column=0)
entry_email = tk.Entry(frame_cliente)
entry_email.grid(row=1, column=1)

label_telefone = tk.Label(frame_cliente, text="Telefone:")
label_telefone.grid(row=2, column=0)
entry_telefone = tk.Entry(frame_cliente)
entry_telefone.grid(row=2, column=1)

label_endereco = tk.Label(frame_cliente, text="Endereço:")
label_endereco.grid(row=3, column=0)
entry_endereco = tk.Entry(frame_cliente)
entry_endereco.grid(row=3, column=1)

#botões
btn_salvar = tk.Button(frame_cliente, text='Salvar', command=inserir_cliente)
btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

# Tabela para exibição dos clientes cadastrados
columns = ('ID', 'Nome', 'E-mail', 'Telefone', 'Endereço')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=1, column=0, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

# Botões de ação para editar e excluir
btn_deletar = tk.Button(janela, text="Excluir", command=delete_cliente)
btn_deletar.grid(row=2, column=0, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text="Atualizar", command=editar_cliente)
btn_atualizar.grid(row=2, column=1, padx=10, pady=10)

# Criar a tabela no banco de dados
criar_tabela()

# Exibir os clientes cadastrados
mostrar_clientes()

# Iniciar a interface gráfica
janela.mainloop()
