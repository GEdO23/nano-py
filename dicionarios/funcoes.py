def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário: ").upper()


def preencher_dicionario(dicionario):
    with (open('bd.txt', 'r') as arquivo):
        # Dividir em uma lista de valor e chave com strip
        for linha in arquivo:
            usuario = linha.split(':')
            lista = formatar_lista_de_arquivo(usuario[1])
            dicionario[usuario[0]] = lista


def formatar_lista_de_arquivo(usuario: str):
    usuario = usuario.replace("[", "")
    usuario = usuario.replace("]", "")
    usuario = usuario.replace("'", "")
    usuario = usuario.replace(" ", "")
    usuario = usuario.replace("\n", "")
    usuario = usuario.split(",")
    return usuario


def inserir(dicionario):
    login = input("Digite o login: ").upper()
    usuario = [input("Digite o nome: ").upper(),
               input("Digite a última data de acesso: "),
               input("Qual a última estação acessada: ").upper()]
    dicionario[login] = usuario
    salvar(login, usuario)


def salvar(chave, valor):
    with open("bd.txt", "a") as arquivo:
        arquivo.write(chave + ":" + str(valor) + "\n")

# def pesquisar(dicionario):
#     with open("bd.txt", "r") as arquivo:
#         for linha in arquivo:
#             if (linha.strip()):
