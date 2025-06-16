
```markdown
# Sistema de Cadastro de Produtos com Python e MySQL

## Descrição
Projeto simples de sistema CRUD para cadastro, listagem e exclusão de produtos, utilizando Python para a interface e MySQL para o banco de dados.

## Funcionalidades
- Cadastrar produto (nome, preço, quantidade)
- Listar todos os produtos cadastrados
- Excluir produto pelo código

## Estrutura do projeto
```

.
├── main.py           # Interface do usuário e menu de opções
├── db.py             # Função para conexão com o banco MySQL
├── produtos.py       # Funções para CRUD no banco de dados

````

## Requisitos
- Python 3.x
- MySQL instalado e rodando localmente
- Biblioteca `mysql-connector-python` instalada
- Banco de dados `cadastro_produtos` criado no MySQL com a tabela `produtos` (descrição abaixo)

## Como instalar dependências

```bash
pip install mysql-connector-python
````

## Estrutura da tabela `produtos` no MySQL

```sql
CREATE TABLE produtos (
    idCodigo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL
);
```

## Como rodar o projeto

1. Certifique-se que o MySQL está rodando e a tabela criada.
2. Clone este repositório.
3. Instale as dependências.
4. Execute o programa:

5. Use o menu para cadastrar, listar e excluir produtos.

## Observações

* O arquivo `db.py` está configurado para conexão local com usuário `root` e sem senha. Ajuste conforme seu ambiente.
* O sistema usa o campo `idCodigo` para identificar produtos na exclusão.

## Exemplo de uso

```
Seja bem vindo ao sistema de cadastro de produtos
Escolha uma opção:
[1] Cadastro de produto
[2] Mostrar produtos cadastrados
[3] Excluir produto
[4] Sair
Digite: 1
Digite o nome do produto: Arroz
Qual valor do Arroz: 12.50
Quantos quer adicionar no estoque: 30

*Produto [Arroz] cadastrado com sucesso*

Escolha uma opção:
[1] Continuar cadastrando
[2] Mostrar produtos cadastrados
[3] Excluir produto
[4] Sair
Digite:
```
