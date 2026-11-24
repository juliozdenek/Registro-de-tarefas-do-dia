biblioteca = [] #lista onde vai ficar salvo os livros cadastrados

opçao = int(input("\n\
Selecione uma opçãon\n\
1 - Adicionar livro\n\
2 - Visualizar estante\n\
3 - Ver quantidade de livros\n\
4 - Verificar se um livro está na estante\n\
5 - Remover livro\n\
0 - Sair"))

while opçao != 0:
    match opçao:
        case 1:
            livro = input("Informe o nome do livro que deseja adicionar")
            if livro not in biblioteca:
                biblioteca.append(livro)
            else :
                print (f"O livro {livro} já existe na biblioteca! ")
        case 2:
            for b in biblioteca:
                print ("b")
        case 3:
            quantidade = len(biblioteca)
            print("len")
        case 4:
            verificar = input("Informe o nome do livro que você deseja verificar: ")
            for b in biblioteca:
                if verificar == b:
                    print("O Livro está na biblioteca")
                else:
                    print("O livro não está na biblioteca")
        case 5:
            pass
        case _:
            print ("opção invalida")
    opçao = int(input("\n\
Selecione uma opçãon\n\
1 - Adicionar livro\n\
2 - Visualizar estante\n\
3 - Ver quantidade de livros\n\
4 - Verificar se um livro está na estante\n\
5 - Remover livro\n\
0 - Sair"))
