from models.produto import Produto
from models.controle_estoque import ControleEstoque

def main():
    controle = ControleEstoque()

    while True:
        print("\n--- Sistema de Controle de Estoque ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            produto = Produto(nome=nome, quantidade=quantidade, preco=preco)
            controle.adicionar_produto(produto)

        elif opcao == "2":
            print("\n--- Lista de Produtos ---")
            controle.listar_produtos()

        elif opcao == "3":
            id = int(input("ID do produto a ser atualizado: "))
            print("Deixe os campos em branco para não alterar.")
            quantidade = input("Nova quantidade: ")
            preco = input("Novo preço: ")
            controle.atualizar_produto(
                id,
                quantidade=int(quantidade) if quantidade else None,
                preco=float(preco) if preco else None
            )

        elif opcao == "4":
            id = int(input("ID do produto a ser removido: "))
            controle.remover_produto(id)

        elif opcao == "5":
            busca = input("Buscar por ID ou Nome? (digite 'id' ou 'nome'): ").lower()
            if busca == "id":
                id = int(input("Digite o ID: "))
                controle.buscar_produto(id=id)
            elif busca == "nome":
                nome = input("Digite o nome: ")
                controle.buscar_produto(nome=nome)

        elif opcao == "6":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()