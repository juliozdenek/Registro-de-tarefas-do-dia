biblioteca = [] #lista onde vai ficar salvo os livros cadastrados

opçao = int(input("\n\
1 - Adicionar livro\n\
2 - Visualizar estante\n\
3 - Ver quantidade de livros\n\
4 - Verificar se um livro está na estante\n\
5 - Remover livro\n\
0 - Sair\n\
    Selecione uma opçao: "))

while opçao != 0:
    match opçao:
        case 1:
            livro = input("Informe o nome do livro que deseja adicionar: ")
            if livro not in biblioteca:
                biblioteca.append(livro)
            else :
                print (f"O livro {livro} já existe na biblioteca! ")
        case 2:
            if len(biblioteca) == 0:
                print("A biblioteca está vazia")
            else:
                for b in biblioteca:
                    print (f"{b}")
        case 3:
            quantidade = len(biblioteca)
            print(f"A biblioteca tem {quantidade} livros")
        case 4:
            verificar = input("Informe o nome do livro que você deseja verificar: ")
            if verificar in biblioteca:

                print("O Livro está na biblioteca")
            else:
                print("O livro não está na biblioteca")
        case 5:
            remover = input("Escolha o livro que você gostaria de remover: ")
            if remover in biblioteca:
                biblioteca.remove(remover)
                print("Livro removido com sucesso!")
            else:
                print("O Livro não está cadastrado.")
    
        case _:
            print ("opção invalida")
    opçao = int(input("\n\
1 - Adicionar livro\n\
2 - Visualizar estante\n\
3 - Ver quantidade de livros\n\
4 - Verificar se um livro está na estante\n\
5 - Remover livro\n\
0 - Sair\n\
    Selecione uma opçao: "))
print ("Programa encerrado, volte sempre!")
