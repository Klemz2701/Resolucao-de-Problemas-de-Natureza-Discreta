# abrir arquivo txt
arq = open("conjuntos.txt", "r")
lista = arq.readlines()

# remover \n da lista
lista_tratada = []

for quebra in lista:
    lista_tratada.append(quebra.replace("\n", ""))

qtd_oper = int(lista_tratada[0])

comprimento = len(lista_tratada)
count_comprimento = int((comprimento - 1) / 3)
count = 1

lista_qtd_oper = []

for i in range(count_comprimento):
    indice = i + count
    count = count + 2
    lista_qtd_oper.append(indice)

for i in lista_qtd_oper:
    tipo_operacao = lista_tratada[i]

    # cria primeiro conjunto
    primeiro_conjunto = []
    for item_primeiro_conjunto in lista_tratada[i + 1].split(", "):
        add_item = item_primeiro_conjunto
        primeiro_conjunto.append(add_item)

    # cria segundo conjunto
    segundo_conjunto = []
    for item_segundo_conjunto in lista_tratada[i + 2].split(", "):
        add_item = item_segundo_conjunto
        segundo_conjunto.append(add_item)

        # União
    conjunto_u = segundo_conjunto
    if tipo_operacao == "U":
        for ni in primeiro_conjunto:
            if not ni in conjunto_u:
                conjunto_u.append(ni)
        print(
            "\nUnião: \nConjunto 1: %s, \nConjunto 2: %s. \nResultado: %s"
            % (primeiro_conjunto, segundo_conjunto, conjunto_u)
        )

        # Interseção
    if tipo_operacao == "I":
        conjunto_i = []
        for i in primeiro_conjunto:
            for ni in segundo_conjunto:
                if i == ni:
                    conjunto_i.append(i)
        print(
            "\nInterseção: \nConjunto 1 %s, \nConjunto 2 %s. \nResultado: %s"
            % (primeiro_conjunto, segundo_conjunto, conjunto_i)
        )

        # Diferença
    conjunto_d = []
    if tipo_operacao == "D":
        for i in primeiro_conjunto:
            if not i in segundo_conjunto:
                conjunto_d.append(i)
        print(
            "\nDiferença: \nConjunto 1 %s, \nConjunto 2 %s. \nResultado: %s"
            % (primeiro_conjunto, segundo_conjunto, conjunto_d)
        )
        # Produto cartesiano
    conjunto_c = []
    if tipo_operacao == "C":
        for i in primeiro_conjunto:
            for ni in segundo_conjunto:
                plano = i, ni
                conjunto_c.append(plano)
        print(
            "\nProduto cartesiano: \nConjunto 1 %s, \nConjunto 2 %s. \nResultado: %s"
            % (primeiro_conjunto, segundo_conjunto, conjunto_c)
        )
