# Inicializa um dicionário vazio que irá armazenar os produtos e seus detalhes (preço e quantidade)
estoque = {} 

# Função para adicionar um produto ao estoque
def adicionar_produto(): 
    # Solicita o nome do produto e o formata com a primeira letra maiúscula
    nome = input("Nome do produto: ").capitalize() 
    # Solicita o preço do produto e converte para float
    preco = float(input("Preço do produto: ")) 
    # Garante que o preço informado seja maior que zero
    while preco <= 0:
        preco = float(input("Por favor, informe um preço válido: ")) 
    # Solicita a quantidade do produto e converte para inteiro
    quantidade = int(input("Quantidade no estoque: ")) 
    # Garante que a quantidade informada seja maior ou igual a zero
    while quantidade < 0:
        quantidade = int(input("Por favor, informe uma quantidade válida: ")) 
    
    # Verifica se o produto já existe no estoque
    if nome in estoque: 
        # Se existir, atualiza a quantidade, mantendo o preço
        estoque[nome] = [estoque[nome][0], estoque[nome][1] + quantidade] 
    else: 
        # Se não existir, adiciona o novo produto com o preço e quantidade informados
        estoque[nome] = [preco, quantidade] 
    print(f"Produto '{nome}' adicionado com sucesso!\n") 

# Função para remover um produto do estoque
def remover_produto(): 
    # Solicita o nome do produto a ser removido e o formata com a primeira letra maiúscula
    nome = input("Nome do produto a remover: ").capitalize() 
    
    # Verifica se o produto existe no estoque
    if nome in estoque: 
        # Se existir, remove o produto do estoque
        del estoque[nome] 
        print(f"Produto '{nome}' removido com sucesso!\n") 
    else: 
        # Se não existir, informa que o produto não foi encontrado
        print(f"Produto '{nome}' não encontrado no estoque.\n") 

# Função para atualizar as informações de um produto
def atualizar_produto():
    # Solicita o nome do produto a ser atualizado
    nome = input("Digite o nome do produto que deseja alterar: ")
    
    # Verifica se o produto existe no estoque
    if nome in estoque:
        # Solicita e armazena o novo nome, preço e quantidade do produto
        novoNome = input("Digite o novo nome do produto: ")
        novoPreco = float(input("Digite o novo preço do produto: "))
        # Garante que o novo preço seja maior que zero
        while novoPreco <= 0:
            novoPreco = float(input("Por favor, digite um preço válido: "))
        novaQuantidade = int(input("Digite a nova quantidade do produto: "))
        # Garante que a nova quantidade seja maior que zero
        while novaQuantidade <= 0:
            novaQuantidade = int(input("Por favor, digite uma quantidade válida: "))

        # Se o novo nome for diferente do nome original, remove o produto antigo e adiciona o novo
        if novoNome != nome:
            del estoque[nome]
            estoque[novoNome] = [novoPreco, novaQuantidade]
        else:
            # Se o nome for o mesmo, apenas atualiza o preço e quantidade
            estoque[nome] = [novoPreco, novaQuantidade]
        print("Produto alterado com sucesso")
    else:
        # Se o produto não existir, informa que não foi encontrado
        print("Produto não encontrado no estoque")

# Função para exibir o estoque atual
def exibir_estoque(): 
    # Verifica se o estoque está vazio
    if not estoque: 
        print("O estoque está vazio.\n") 
    else: 
        # Exibe a lista de produtos, com seus preços e quantidades
        print("\nEstoque atual:") 
        for produto, detalhes in estoque.items(): 
            print(f"Produto: {produto} | Preço: R${detalhes[0]} | Quantidade: {detalhes[1]}") 
        print()

# Função para calcular o valor total do estoque
def calcular_valor_total(): 
    # Calcula o valor total, somando o preço multiplicado pela quantidade de cada produto
    valor_total = sum(preco * quantidade for preco, quantidade in estoque.values()) 
    print(f"\nValor total do estoque: R${valor_total:.2f}\n") 

# Função principal que exibe o menu e chama as funções apropriadas
def main(): 
    while True: 
        # Exibe as opções do menu
        print("1. Adicionar produto") 
        print("2. Remover produto") 
        print("3. Exibir estoque") 
        print("4. Alterar produto") 
        print("5. Calcular valor total do estoque") 
        print("6. Sair") 

        # Solicita que o usuário escolha uma opção
        escolha = input("Escolha uma opção (1-6): ") 

        # Executa a função correspondente à escolha do usuário
        if escolha == '1':
            adicionar_produto()
        elif escolha == '2':
            remover_produto()
        elif escolha == '3':
            exibir_estoque()
        elif escolha == '4':
            atualizar_produto()
        elif escolha == '5':
            calcular_valor_total()
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            # Informa que a opção é inválida se o usuário inserir algo diferente de 1 a 6
            print("Opção inválida. Tente novamente.\n")

# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == "__main__":
    main()
