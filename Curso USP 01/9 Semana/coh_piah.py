import re
import math

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    f = 0
    assinatura_texto = as_a
    assinatura_padrao = as_b
    for n in range(0, len(assinatura_texto)):
        f += math.fabs(assinatura_texto[n]-assinatura_padrao[n])
    sa_b = f / 6
    #print(sa_b)
    return sa_b


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #print('entrei na função')
    #print(f'o texto a ser analisado é {[texto]}')
    texto_analisado = gera_lista_de_palavras([texto])
    #print(f'texto analisado, sua lista de sentenças é { texto_analisado[0]}, sua lista de frases é {texto_analisado[1]}, e a lista de palavras é {texto_analisado[2]}')
    lista_tam_med_palavras = gera_lista_tam_palavras(texto_analisado[2])
    #print(f'lista de palavras gerada é {texto_analisado[2]}')
    tam_med_palavras = media_palavras(lista_tam_med_palavras)
    #print(f'tamanho medio de palavras calculada')
    rtt = relacao_type_token(texto_analisado[2])
    #print(f'relaxao type')
    rhl = razao_hepax_legomana(texto_analisado[2])
    #print(f'Razao')
    tms = tam_med_sent(texto_analisado[0])
    cs = complex_sentenca(texto_analisado[0], texto_analisado[1])
    t_med_frase = tam_med_frase(texto_analisado[1])
    #print('analise terminada')
    return tam_med_palavras, rtt, rhl, tms, cs, t_med_frase


def avalia_textos(textos, ass_cp):
    ''''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura = ass_cp
    lista_texto = textos
    lista_resul_textos = []
    lista_resul_compa = []
    #print(lista_texto)
    for textos in range(0, len(lista_texto)):
        #print(f'o texto avaliado é: {lista_texto[textos]}')
        resultado = calcula_assinatura(lista_texto[textos])
        #print(resultado)
        lista_resul_textos.append(resultado)
    #print(lista_resul_textos)
    for resultados in range(0, len(lista_resul_textos)):
        resultado = compara_assinatura(lista_resul_textos[resultados], assinatura)
        lista_resul_compa.append(resultado)
    posicao = comparacao(lista_resul_compa)
    #print(lista_resul_compa)
    return posicao + 1


def comparacao(lista_de_comparacao):
    maior_prop = min(lista_de_comparacao)
    for resultado in range(0, len(lista_de_comparacao)):
        if maior_prop == lista_de_comparacao[resultado]:
            return resultado


def gera_lista_de_palavras (lista_texto):
    lista_sentencas = []
    lista_frases = []
    lista_palavras = []
    lista_texto = lista_texto
    loop = 0
    iteracao = len(lista_texto)
    contador = True
    while contador == True:
        lista_sentencas = separa_sentencas(lista_texto[loop])
        #print(f'a lista de sentenças é {lista_sentencas}')
        for sentencas in range(0, len(lista_sentencas)):
            temp_frases = separa_frases(lista_sentencas[sentencas])
            lista_frases += temp_frases
        #print(f'a lista de frasese é {lista_frases}')
        for sentencas in range(0, len(lista_frases)):
            temp = separa_palavras(lista_frases[sentencas])
            lista_palavras += temp
        loop += 1
        if loop == iteracao: contador = False
    #print(f'A lista de palavras é {lista_palavras}')
    return lista_sentencas, lista_frases, lista_palavras


def gera_lista_tam_palavras(lista_palavras):
    lista_tam_palavras = []
    for palavras in range(0, len(lista_palavras)):
        lista_tam_palavras.append(len(lista_palavras[palavras]))
    return lista_tam_palavras


def media_palavras(lista_comrp_palavras):
    lista_de_palavras = lista_comrp_palavras
    media_simples = math.fsum(lista_de_palavras) / len(lista_de_palavras)
    return media_simples


def relacao_type_token(lista_palavras):
    lista_palavras = lista_palavras
    #print(lista_palavras)
    #print(len(lista_palavras))
    rtp = n_palavras_diferentes(lista_palavras)/len(lista_palavras)
    #print(rtp)
    return rtp


def razao_hepax_legomana(lista_palavras):
    lista_palavras = lista_palavras
    rhl = n_palavras_unicas(lista_palavras)/len(lista_palavras)
    return rhl


def tam_med_sent(lista_setenca):
    lista_setenca = lista_setenca
    somatorio_tam_sent = 0
    for sentencas in range(0, len(lista_setenca)):
        somatorio_tam_sent += len(lista_setenca[sentencas])
    med = somatorio_tam_sent/len(lista_setenca)
    return med


def complex_sentenca(lista_sentenca, lista_frases):
    complex = len(lista_frases)/len(lista_sentenca)
    return complex


def tam_med_frase(lista_frase):
    lista_frase = lista_frase
    somatorio_tam_frase = 0
    for frases in range(0, len(lista_frase)):
        somatorio_tam_frase += len(lista_frase[frases])
    med = somatorio_tam_frase / len(lista_frase)
    #print(med)
    return med

assinatura = le_assinatura()
lista_texto = le_textos()
lista_palavras = gera_lista_de_palavras(lista_texto)
max_prop = avalia_textos(lista_texto, assinatura)
print(f'O autor do texto {max_prop} está infectado com COH-PIAH')







