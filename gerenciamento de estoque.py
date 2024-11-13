# Classe Produto
class Produto:
    def __init__(self, id_produto, nome, quantidade, preco, descricao):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao

# Classe Cliente
class Cliente:
    def __init__(self, id_cliente, nome, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email

# Listas para armazenar produtos e clientes
produtos = []
clientes = []

# Funções para gerenciar produtos
def adicionar_produto(id_produto, nome, quantidade, preco, descricao):
    produto = Produto(id_produto, nome, quantidade, preco, descricao)
    produtos.append(produto)

def listar_produtos():
    for produto in produtos:
        print(f"ID: {produto.id_produto}, Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: R${produto.preco:.2f}, Descrição: {produto.descricao}")

def atualizar_produto(id_produto, nome, quantidade, preco, descricao):
    for produto in produtos:
        if produto.id_produto == id_produto:
            produto.nome = nome
            produto.quantidade = quantidade
            produto.preco = preco
            produto.descricao = descricao
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def remover_produto(id_produto):
    global produtos
    produtos = [produto for produto in produtos if produto.id_produto != id_produto]
    print("Produto removido com sucesso!")

# Funções para gerenciar clientes
def adicionar_cliente(id_cliente, nome, email):
    cliente = Cliente(id_cliente, nome, email)
    clientes.append(cliente)

def listar_clientes():
    for cliente in clientes:
        print(f"ID: {cliente.id_cliente}, Nome: {cliente.nome}, Email: {cliente.email}")

def atualizar_cliente(id_cliente, nome, email):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            cliente.nome = nome
            cliente.email = email
            print("Cliente atualizado com sucesso!")
            return
    print("Cliente não encontrado.")

def remover_cliente(id_cliente):
    global clientes
    clientes = [cliente for cliente in clientes if cliente.id_cliente != id_cliente]
    print("Cliente removido com sucesso!")

# Menu principal
def menu():
    while True:
        print("\nMenu de Gerenciamento:")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("5 - Adicionar Cliente")
        print("6 - Listar Clientes")
        print("7 - Atualizar Cliente")
        print("8 - Remover Cliente")
        print("9 - Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            id_produto = int(input("ID do Produto: "))
            nome = input("Nome do Produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            descricao = input("Descrição: ")
            adicionar_produto(id_produto, nome, quantidade, preco, descricao)
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            id_produto = int(input("ID do Produto a ser atualizado: "))
            nome = input("Novo Nome do Produto: ")
            quantidade = int(input("Nova Quantidade: "))
            preco = float(input("Novo Preço: "))
            descricao = input("Nova Descrição: ")
            atualizar_produto(id_produto, nome, quantidade, preco, descricao)
        elif opcao == 4:
            id_produto = int(input("ID do Produto a ser removido: "))
            remover_produto(id_produto)
        elif opcao == 5:
            id_cliente = int(input("ID do Cliente: "))
            nome = input("Nome do Cliente: ")
            email = input("Email: ")
            adicionar_cliente(id_cliente, nome, email)
        elif opcao == 6:
            listar_clientes()
        elif opcao == 7:
            id_cliente = int(input("ID do Cliente a ser atualizado: "))
            nome = input("Novo Nome do Cliente: ")
            email = input("Novo Email: ")
            atualizar_cliente(id_cliente, nome, email)
        elif opcao == 8:
            id_cliente = int(input("ID do Cliente a ser removido: "))
            remover_cliente(id_cliente)
        elif opcao == 9:
            print("Saindo do programa... Programa encerrado com sucesso.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    input("\nPressione Enter para encerrar o programa...")

# Executar o menu principal
menu()
