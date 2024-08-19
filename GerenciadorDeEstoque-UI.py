# Importando bibliotecas necessárias para a interface gráfica e mensagens de diálogo
import tkinter as tk
from tkinter import messagebox

# Classe Produto representa um item no estoque
class Produto:
    # Método construtor que define os atributos de cada produto: nome, preço e quantidade
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

# Classe Estoque para gerenciar uma coleção de produtos
class Estoque:
    # Método construtor que inicializa o estoque como um dicionário vazio
    def __init__(self):
        self.produtos = {}

    # Método para adicionar um novo produto ao estoque
    def adicionar_produto(self, nome, preco, quantidade):
        # Verifica se o produto já existe no estoque
        if nome in self.produtos:
            # Se existir, aumenta a quantidade do produto
            self.produtos[nome].quantidade += quantidade
        else:
            # Se não existir, cria um novo produto e adiciona ao estoque
            self.produtos[nome] = Produto(nome, preco, quantidade)

    # Método para remover um produto do estoque
    def remover_produto(self, nome):
        # Verifica se o produto existe no estoque
        if nome in self.produtos:
            # Se existir, remove o produto do estoque
            del self.produtos[nome]
            return True  # Retorna True indicando sucesso
        else:
            # Se não existir, retorna False indicando falha
            return False

    # Método para atualizar o preço e a quantidade de um produto existente
    def atualizar_produto(self, nome, preco, quantidade):
        # Verifica se o produto existe no estoque
        if nome in self.produtos:
            # Se existir, atualiza o preço e a quantidade do produto
            self.produtos[nome].preco = preco
            self.produtos[nome].quantidade = quantidade
            return True  # Retorna True indicando sucesso
        else:
            # Se não existir, retorna False indicando falha
            return False

    # Método para exibir todos os produtos no estoque
    def exibir_estoque(self):
        # Retorna uma lista de tuplas contendo o nome, preço e quantidade de cada produto
        return [(produto.nome, produto.preco, produto.quantidade) for produto in self.produtos.values()]

    # Método para calcular o valor total do estoque
    def calcular_valor_total(self):
        # Retorna a soma do preço multiplicado pela quantidade de todos os produtos no estoque
        return sum(produto.preco * produto.quantidade for produto in self.produtos.values())

# Função para adicionar um novo produto através da interface gráfica
def adicionar_produto():
    # Captura os valores dos campos de entrada
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    quantidade = int(entry_quantidade.get())

    # Chama o método adicionar_produto da classe Estoque
    estoque.adicionar_produto(nome, preco, quantidade)

    # Exibe uma mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado ao estoque.")

    # Atualiza a lista de produtos exibida
    atualizar_lista()

# Função para remover um produto através da interface gráfica
def remover_produto():
    # Captura o nome do produto a ser removido
    nome = entry_nome.get()
    # Verifica se a remoção foi bem-sucedida e exibe a mensagem correspondente
    if estoque.remover_produto(nome):
        messagebox.showinfo("Sucesso", f"Produto '{nome}' removido do estoque.")
    else:
        messagebox.showerror("Erro", f"Produto '{nome}' não encontrado.")
    # Atualiza a lista de produtos exibida
    atualizar_lista()

# Função para atualizar um produto através da interface gráfica
def atualizar_produto():
    # Captura os valores dos campos de entrada
    nome = entry_nome.get()
    preco = float(entry_preco.get())
    quantidade = int(entry_quantidade.get())
    # Verifica se a atualização foi bem-sucedida e exibe a mensagem correspondente
    if estoque.atualizar_produto(nome, preco, quantidade):
        messagebox.showinfo("Sucesso", f"Produto '{nome}' atualizado.")
    else:
        messagebox.showerror("Erro", f"Produto '{nome}' não encontrado.")
    # Atualiza a lista de produtos exibida
    atualizar_lista()

# Função para atualizar a lista de produtos exibida na interface gráfica
def atualizar_lista():
    # Limpa a lista de exibição
    listbox_estoque.delete(0, tk.END)
    # Adiciona cada produto do estoque na lista de exibição
    for produto in estoque.exibir_estoque():
        listbox_estoque.insert(tk.END, f"Produto: {produto[0]}, Preço: R${produto[1]:.2f}, Quantidade: {produto[2]}")

# Função para calcular o valor total do estoque e exibir em uma mensagem
def calcular_valor_total():
    valor_total = estoque.calcular_valor_total()
    messagebox.showinfo("Valor Total", f"Valor total do estoque: R${valor_total:.2f}")

# Configuração da Janela Principal usando tkinter
root = tk.Tk()
root.title("Gerenciamento de Estoque")

# Criando um frame para organizar as entradas de dados
frame = tk.Frame(root)
frame.pack(pady=10)

# Labels e campos de entrada para nome, preço e quantidade dos produtos
tk.Label(frame, text="Nome do Produto:").grid(row=0, column=0)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1)

tk.Label(frame, text="Preço:").grid(row=1, column=0)
entry_preco = tk.Entry(frame)
entry_preco.grid(row=1, column=1)

tk.Label(frame, text="Quantidade:").grid(row=2, column=0)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=2, column=1)

# Frame para organizar os botões de ação
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

# Botões para adicionar, remover, atualizar produtos e calcular valor total
btn_adicionar = tk.Button(frame_btn, text="Adicionar Produto", command=adicionar_produto)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_remover = tk.Button(frame_btn, text="Remover Produto", command=remover_produto)
btn_remover.grid(row=0, column=1, padx=5)

btn_atualizar = tk.Button(frame_btn, text="Atualizar Produto", command=atualizar_produto)
btn_atualizar.grid(row=0, column=2, padx=5)

btn_valor_total = tk.Button(frame_btn, text="Calcular Valor Total", command=calcular_valor_total)
btn_valor_total.grid(row=0, column=3, padx=5)

# Listbox para exibir a lista de produtos do estoque
listbox_estoque = tk.Listbox(root, width=50)
listbox_estoque.pack(pady=10)

# Inicializa o estoque
estoque = Estoque()

# Inicia o loop principal da interface gráfica
root.mainloop()

"""
Uso da Biblioteca tkinter:

Este código utiliza a biblioteca `tkinter` para criar uma interface gráfica (GUI) para gerenciar o estoque de uma loja.
O `tkinter` é uma biblioteca padrão do Python usada para criar interfaces gráficas. Ela fornece uma variedade de widgets,
como botões, labels, entradas de texto, e muito mais.

### Principais Componentes usados da Interface Gráfica:

1. **Janela Principal (`root`)**:
   - A janela principal (`Tk()`) é a base da aplicação, onde todos os widgets são adicionados.

2. **Frames**:
   - Os frames (`Frame`) são usados para organizar os widgets em grupos. Neste código, são utilizados dois frames:
     - `frame`: contém as labels e os campos de entrada para nome, preço e quantidade.
     - `frame_btn`: contém os botões para adicionar, remover, atualizar produtos e calcular o valor total do estoque.

3. **Entradas de Texto (`Entry`)**:
   - Os campos de entrada (`Entry`) permitem ao usuário inserir informações sobre os produtos (nome, preço e quantidade).

4. **Labels**:
   - As labels (`Label`) são usadas para identificar os campos de entrada, como "Nome do Produto", "Preço" e "Quantidade".

5. **Botões (`Button`)**:
   - Os botões (`Button`) executam funções específicas quando clicados. Neste código, há botões para adicionar, remover, atualizar produtos e calcular o valor total do estoque.

6. **Lista de Produtos (`Listbox`)**:
   - A lista (`Listbox`) exibe os produtos atualmente no estoque, mostrando nome, preço e quantidade.


Obs.: Essa biblioteca não precisa de intalação. Ela já vem embutida no Python.
"""
