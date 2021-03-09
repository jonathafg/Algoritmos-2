#Atividade

#Construir um algoritmo que contenha 3 listas

#- Nomes de produtos
#- Preços de cada produto
#- Quantidades de cada produto

#Construir uma função para imprimir um dos produtos da lista e uma
#Função para retirar um dos produtos das listas

Nome_Produtos = ["Refrigerante", "Salsicha", "Miojo"]
Preco_produtos = ["5.5", "3.8", "1.5"]
Qtd_Produtos = ["9", "22", "6"]


def imprimir_produto (Nome_Produtos, Preco_produtos, Qtd_Produtos):
    print ("Lista de Produtos: ")
    print("",Nome_Produtos)
    produto = input("\nQual Produto você deseja ver mais informacoes ? ")
    posicao = Nome_Produtos.index(produto)
    print ("\nProduto: ", Nome_Produtos[posicao])
    print ("Preco: ", Preco_produtos[posicao])
    print ("Quantidade: ", Qtd_Produtos[posicao])

def apagar_produto (Nome_Produtos, Preco_produtos, Qtd_Produtos):
    print ("\nLista de Produtos: ")
    print("",Nome_Produtos)
    produto = input("\nQual Produto você deseja remover ? ")
    posicao = Nome_Produtos.index(produto)
    del (Nome_Produtos[posicao])
    del (Preco_produtos[posicao])
    del(Qtd_Produtos[posicao])
    print("\nProduto removido! \n", Nome_Produtos)


#Imprimir Produto conforme solicitação do usuário
imprimir_produto(Nome_Produtos, Preco_produtos, Qtd_Produtos)

#Apagar produto conforme solicitação do usuário
apagar_produto(Nome_Produtos, Preco_produtos, Qtd_Produtos)





