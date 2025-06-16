#Conexao com o servidor MYSQL

import mysql.connector #Biblioteca do MYSQL

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',#User do banco de dados
        password='', #Senha do banco de dados
        database='cadastro_produtos' #Nome do banco de dados
    )