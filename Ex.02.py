#  Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
#  além de informar a quantidade de vezes em que ela ocorre. 

def verificar_a(texto):
    # Converte a string para minúsculas e conta quantas vezes 'a' aparece
    contador = texto.lower().count('a')
    return contador

while True:
    texto = input("Informe uma Palavra (string): ")

    # Verifica a quantidade de vezes que a letra 'a' aparece
    quantidade = verificar_a(texto)
    
    # Exibe o resultado
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vezes na palavra digitada.")
    else:
        print("A letra 'a' não aparece na palavra digitada.")

    # Pergunta se o usuário deseja continuar ou encerrar
    continuar = input("Deseja verificar outra Palavra (string)? (s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado.")
        break
