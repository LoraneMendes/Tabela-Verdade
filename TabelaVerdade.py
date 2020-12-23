variaveis = []
operadores = ["&", "|", ">", "=", "~"]
resultados = []

print("Regras:\n&  para indicar conjunção\n|  para indicar disjunção\n>  para indicar condicional\n=  para indicar bicondicional\n~  para indicar negação")
while True:
    input_vars = (str(input("Digite a formula: ")))
    print("\n")
    string = ""
    for e in input_vars:
        if e in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" and e not in variaveis:
            variaveis.append(e)
    for e in input_vars:
        string += (e + " ")
    string = string.split()
    if any(x in operadores for x in string):
        break


resultado_Tabela = [True, False]


array = []
for i in range(2 ** len(variaveis)):
    array.append([])

contador_tabela = len(variaveis)
for i in range(len(variaveis)):
    contador = 0
    while contador < len(array):
        for i in range((2 ** len(variaveis)) // (2 ** contador_tabela)):
            array[contador].insert(0, resultado_Tabela[0])
            contador += 1
        for i in range((2 ** len(variaveis)) // (2 ** contador_tabela)):
            array[contador].insert(0, resultado_Tabela[1])
            contador += 1
    contador_tabela -= 1

string = ""
for e in input_vars:
    string += (e + " ")
string = string.split()


def string_funcional(j):
    dic = {}
    for i in range(len(variaveis)):
        dic[str(variaveis[i])] = array[j][i]
    return dic



def negacao(x):
    return not x


def calcula_negacao(string):
    for i in range(len(string)):
        if string[i] == '~':
            string[i] = ""
            string[i + 1] = negacao(string[i + 1])
    return string


def calcula_and(string):
    for i in range(len(string)):
        if string[i] == '&':
            string[i], string[i - 1], string[i + 1] = "", "", string[i - 1] & string[i + 1]
    return string


def calcula_or(string):
    for i in range(len(string)):
        if string[i] == '|':
            string[i], string[i - 1], string[i + 1] = "", "", string[i - 1] | string[i + 1]
    return string


def resolve_condicional(string):
    for i in range(len(string)):
        if string[i] == '>':
            string[i], string[i - 1], string[i + 1] = "", "", formula_condicional(string[i - 1], string[i + 1])
    return string


def formula_condicional(a, b):
    return not a or b


def formula_bicondicional(a,b):
    return a == b


def resolve_bicondicional(string):
    for i in range(len(string)):
        if string[i] == '=':
            string[i], string[i - 1], string[i + 1] = "", "", formula_bicondicional(string[i-1], string[i+1])
    return string


def remove_espacos(string):
    for e in string:
        if e == "":  # swap for list comprehension here
            string.remove("")
            remove_espacos(string)
    return string


def main(string):
    calcula_negacao(string)
    remove_espacos(string)
    calcula_and(string)
    remove_espacos(string)
    calcula_or(string)
    remove_espacos(string)
    remove_espacos(string)
    resolve_condicional(string)
    remove_espacos(string)
    resolve_bicondicional(string)
    remove_espacos(string)
    resultados.append(string[0])


def cria_ordem(dic):
    string2 = []
    for e in string:
        if e in dic:
            string2.append(dic[e])
        else:
            string2.append(e)
    return string2


def mainmain():
    for j in range(len(array)):
        dic = string_funcional(j)
        string = cria_ordem(dic)
        main(string)


mainmain()


print(variaveis, input_vars)
for i in range(len(array)):
    print(array[i],resultados[i])

encerrar = input("\nPressione [Enter] para encerrar")
