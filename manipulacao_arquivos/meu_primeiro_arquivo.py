with open('primeiro_arquivo.txt', 'w') as arquivo:
    arquivo.write('Hello World!')

with open('primeiro_arquivo.txt', 'a') as arquivo:
    arquivo.write('\nHow are you?')