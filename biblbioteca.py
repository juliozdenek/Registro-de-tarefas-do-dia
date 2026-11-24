livros = [] #lista onde vai ficar salvo os livros cadastrados
opçao = input("Digite uma opçao: " )

while opçao != "0":
    
    print("=== ESTANTE DE LIVROS ===")
    print("1 - Adicionar livro")
    print("2 - Visualizar estante")
    print("3 - Ver quantidade de livros")
    print("4 - Verificar se um livro está na estante")
    print("5 - Remover livro")
    print("0 - Sair")
    
    if opçao == "1":
        livro = input("Digite o nome do livro: " )
    
        if livro not in livros:
            livros.append(livro)
            print("Livro adicionado com sucesso!")
        else: 
            print("Erro ao adicionar o livro")
        
        

            
    