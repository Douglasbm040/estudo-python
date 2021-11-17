def verifica_armistrong(num):
    digito=str(num)
    n_digito=len(digito)
    vetor = []
    for i in range(0,len(digito)):
        vetor.append(int(digito[i])**n_digito)
    total= sum(vetor)
    if (total==num):
       return print("o numero {} e um numero armstrong",num)
    else:
        return print("o numero {} nao e numero de armstrong",num)
verifica_armistrong(9)

