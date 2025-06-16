from produto import cadastrarProduto, lerProdutos, excluirProduto

print("Seja bem vindo ao sistema de cadastro de produtos")
escolha = int(input("Escolha uma opção:\n"
                    "[1] Cadastro de produto\n"
                    "[2] Mostrar produtos cadastrados\n"
                    "[3] Excluir produto\n"
                    "[4] Sair\n"
                    "Digite: "))

while True:
    if escolha == 1:
        nome = str(input("Digite o nome do produto: "))
        preco = float(input(f"Qual valor do {nome}: "))
        quantidade = int(input("Quantos quer adicionar no estoque: "))
        print("")
        cadastrarProduto(nome, preco, quantidade)
        print(f"PRODUTO [{nome}] CADASTRADO COM SUCESSO!\n")
        escolha = int(input("Escolha uma opção:\n"
                            "[1] Continuar cadastrando\n"
                            "[2] Mostrar produtos cadastrados\n"
                            "[3] Excluir produto\n"
                            "[4] Sair\n"
                            "Digite: "))
    elif escolha == 2:
        lerProdutos()
        escolha = int(input("Escolha uma opção:\n"
                            "[1] Cadastrar novo produto\n"
                            "[2] Mostrar produtos cadastrados\n"
                            "[3] Excluir produto\n"
                            "[4] Sair\n"
                            "Digite: "))
    elif escolha == 3:
        lerProdutos()
        nomeDoProdutoParaExcluir = str(input("Qual Codigo do produto que deseja excluir: "))
        excluirProduto(nomeDoProdutoParaExcluir)
        escolha = int(input("Escolha uma opção:\n"
                            "[1] Cadastrar novo produto\n"
                            "[2] Mostrar produtos cadastrados\n"
                            "[3] Excluir produto\n"
                            "[4] Sair\n"
                            "Digite: "))
    else:
        print("")
        print("Sistema finalizado, volte sempre!")
        break