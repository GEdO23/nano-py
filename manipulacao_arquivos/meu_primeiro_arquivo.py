with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Hello World!')

with open('arquivo.txt', 'a') as arquivo:
    arquivo.write('\nHow are you?')

with open("arquivo.txt", "r") as arquivo:
    # conteudo = arquivo.read()
    # conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)
