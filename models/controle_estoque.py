import sqlite3

class ControleEstoque:
    def __init__(self, loja="loja.db"):
        self.conn = sqlite3.connect(loja)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                quantidade INTEGER NOT NULL,
                                preco REAL NOT NULL)''')
    
    def _executar_query(self, query, params=()):
        with self.conn:
            return self.conn.execute(query, params)

    def adicionar_produto(self, nome, quantidade, preco):
        self._executar_query("INSERT INTO Produtos (nome, quantidade, preco) VALUES (?, ?, ?)", (nome, quantidade, preco))
        print("Produto adicionado com sucesso!")

    def listar_produtos(self):
        produtos = self._executar_query("SELECT * FROM Produtos").fetchall()
        if produtos:
            for prod in produtos:
                print(f"ID: {prod[0]}, Nome: {prod[1]}, Quantidade: {prod[2]}, Preço: R${prod[3]:.2f}")
        else:
            print("Estoque vazio!")

    def atualizar_produto(self, id, quantidade=None, preco=None):
        if quantidade is not None:
            self._executar_query("UPDATE Produtos SET quantidade = ? WHERE id = ?", (quantidade, id))
        if preco is not None:
            self._executar_query("UPDATE Produtos SET preco = ? WHERE id = ?", (preco, id))
        print("Produto atualizado com sucesso!")

    def remover_produto(self, id):
        self._executar_query("DELETE FROM Produtos WHERE id = ?", (id,))
        print("Produto removido com sucesso!")

    def buscar_produto(self, id=None, nome=None):
        query = "SELECT * FROM Produtos WHERE id = ? OR nome LIKE ?"
        params = (id, f"%{nome}%" if nome else "%")
        produto = self._executar_query(query, params).fetchone()
        if produto:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: R${produto[3]:.2f}")
        else:
            print("Produto não encontrado!")
