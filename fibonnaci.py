def is_fibonacci(n):
    if n < 0:
        return False
    
    # Função para gerar números de Fibonacci
    def fibonacci_sequence():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    # Gerar números de Fibonacci até encontrar o número n ou ultrapassá-lo
    for fib_num in fibonacci_sequence():
        if fib_num == n:
            return True
        if fib_num > n:
            return False

# Função principal
def main():
    try:
        num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if is_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()



def verificar_letra_a(s):
    # Converte a string para minúsculas para garantir que a contagem seja case-insensitive
    s = s.lower()
    
    # Conta a quantidade de vezes que a letra 'a' aparece na string
    quantidade = s.count('a')
    
    # Verifica se a letra 'a' está presente na string
    if quantidade > 0:
        print(f"A letra 'a' (ou 'A') está presente {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' (ou 'A') não está presente na string.")

# Função principal
def main():
    s = input("Digite uma string para verificar a presença da letra 'a': ")
    verificar_letra_a(s)

if __name__ == "__main__":
    main()

