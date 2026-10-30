agenda = {}

def adicionar_ctt(agenda, nome, numero):
    if numero in agenda.values():
        print("Esse número já foi salvo")

    else:
        agenda[nome] = numero
        print(agenda)

    return

def buscar_ctt(agenda, nome):
    if nome not in agenda:
        print("Esse contato não existe")

    else:
        print(agenda[nome])

def deletar_ctt(agenda, nome):
    if nome not in agenda:
        print("Esse contato não existe")
    else:
        del agenda[nome]
        print("Contato apagado.")


adicionar_ctt(agenda, "Joao", 992210125)
print(agenda)