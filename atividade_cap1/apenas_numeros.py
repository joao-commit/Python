def ler_numeros():
    numeros = []
    
    print("--- Leitor de Números Iniciado ---")
    
    while True:
        entrada = input("Digite um número (ou uma letra para sair): ")
        
        try:
            # Tenta converter a entrada para um número decimal
            numero = float(entrada)
            numeros.append(numero)
            print(f"✅ Número {numero} registrado com sucesso!")
            
        except ValueError:
            # Captura o erro se a conversão falhar (ex: usuário digitou texto)
            print("\n❌ Ops! Você digitou um valor que não é um número.")
            print("Encerrando a leitura. Muito obrigado por utilizar o sistema!")
            break  # Interrompe o laço while