# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

def fibonacci(n):
    if n < 0:
        return False  # Não há números negativos na sequência de Fibonacci
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True  # Se o número informado estiver na sequência, retorna True
        a, b = b, a + b
    return False  # Se o número não estiver na sequência, retorna False

while True:
    # Garantir que o usuário informe um número positivo
    while True:
        numero = int(input("Informe um número positivo: "))
        if numero >= 0:
            break  
        else:
            print("Por favor, informe um número positivo.")

    # Verifica se o número está na sequência de Fibonacci
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
    continuar = input("Deseja verificar outro número? (s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado.")
        break
