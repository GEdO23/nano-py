# Criando variáveis
nome = input('Digite um funcionário: ')  # String (sequencia de caracteres)
empresa = input("Digite uma instituição: ")  # String (sequencia de caracteres)
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))  # Número inteiro
mediaMensalidade = float(input("Digite a média da mensalidade: "))  # Número flutuante

# Informando valores
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

# Informando tipos de valores
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))
