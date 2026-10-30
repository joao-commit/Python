def verificar_parenteses(expressao):
    parenteses = []
    for caractere in expressao:
        if caractere == ("("):
            parenteses.append(caractere)
        elif caractere == (")"):
            parenteses.pop()
    if not parenteses:
        return print("Os parenteses estão bem fechados")
    return print("Os parenteses não estão bem fechados")

verificar_parenteses("((2+8)*6(4+5)+(12/3))")