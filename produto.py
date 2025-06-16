from fileinput import close

from db import conectar

def cadastrarProduto(nome, preco, quantidade):
    conexao =  conectar() #Conectar ao banco de dados MYSQl pelo arquivo 'db.py'
    cursor = conexao.cursor() #Inicia possibilidade de enviar uma query para o banco de dados MYSQL
    sql = "INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)" #Query
    valores = (nome, preco, quantidade) #Tupla que recebe valores para query
    cursor.execute(sql, valores) #Enviar a query para o banco de dados MYSQL com query na variavel "sql" e a tupla com seus valores na variavel "valores"
    conexao.commit() #Confirma e grava a query no banco MYSQL
    print(f"*Produto [{nome}] cadastrado com sucesso*\n")

    # Importante fechar esses dois termos abertos
    cursor.close() #Fecha possivilidade de enviar query
    conexao.close() #Fecha conexão com banco de dados MYSQL do arquivo 'db.py'

def lerProdutos():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)

    produtos = cursor.fetchall() #Retorna todas as linhas(registros) da tabela do banco MYSQL
    for id, nome, preco, quantidade in produtos: #Laço para printar cada linha(registro) da tabela do banco MYSQL
        print(f"Codigo: {id} -- Nome: {nome} -- Preço: R${float(preco)} -- Quantidade: {quantidade}")
    print("\n")

    cursor.close()
    conexao.close()

def excluirProduto(nome):
    conexao =  conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM produtos WHERE idCodigo = %s "
    valores = (nome, )
    cursor.execute(sql, valores)
    conexao.commit()
    print(f"*Produto excluido com sucesso*\n")
    cursor.close()
    conexao.close()