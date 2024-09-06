# explicando o exercício:

t = [[3-i for i in range (3)] for j in range (3)]
# a primeira linha cria uma lista comprimida de duas dimensões
# o range i cria a primeira linha
# o range j replica a matriz
print(t)
# t se parece com o visto abaixo:
# t = [3, 2, 1], [3, 2, 1], [3, 2, 1]

s = 0
for i in range(3):
    s += t[i][i]
    print(s) 
# a matriz é referida por 2 índices, por ter 2 dimensões
# s recebe a cada iteração a posição em que está apontado, em linha e coluna