import os

os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela antes do jogo começar
palavra_secreta = input("Digite a palavra secreta (Não pode conter espaços): ").upper() # Converte a palavra secreta para maiúscula
os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela para que a palavra secreta não fique visível
while len(palavra_secreta) == 0 or not palavra_secreta.isalpha(): # Verifica se a palavra secreta contém espaços e se não está vazia
    if len(palavra_secreta) == 0:
        print("A palavra secreta não pode ser vazia.")
    elif not palavra_secreta.isalpha():
        print("A palavra secreta não pode conter caracteres que não sejam letras.")
    else:
        print("A palavra secreta não pode conter espaços.")
    palavra_secreta = input("Digite a palavra secreta (Não pode conter espaços): ").upper()
    os.system('cls' if os.name == 'nt' else 'clear')

letras_diferentes = len(set(palavra_secreta)) # Conta a quantidade de letras diferentes na palavra secreta

# Define o total de tentativas
tentativas_total_str = input(f"Digite a quantidade de tentativas que vai ter (Tem que ter no mínimo {letras_diferentes} tentativas) : ")
os.system('cls' if os.name == 'nt' else 'clear')

while tentativas_total_str.isdigit() == False: # Verifica se o usuário digitou um número inteiro
    print("Por favor, digite apenas números inteiros.")
    tentativas_total_str = input(f"Digite a quantidade de tentativas que vai ter (Tem que ter no mínimo {letras_diferentes} tentativas) : ")
    os.system('cls' if os.name == 'nt' else 'clear')

tentativas_total = int(tentativas_total_str)

while tentativas_total < letras_diferentes: # Verifica se o número de tentativas é menor que o número de letras diferentes da palavra secreta
    print("Impossivel que o usuario ganhe o jogo com menos tentativas que letras diferentes na palavra secreta.")
    print(f"Tem que ser mais que {letras_diferentes} tentivas")
    tentativas_total = int(input("Digite a quantidade de tentativas que vai ter: "))
    os.system('cls' if os.name == 'nt' else 'clear')

palavra_descoberta = ""
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ").upper() # Converte a letra digitada para maiúscula
    while len(letra_digitada) != 1 or not letra_digitada.isalpha(): # Verifica se o usuário digitou apenas uma letra e se é uma letra do alfabeto
        if len(letra_digitada) != 1:
            print("Por favor, digite apenas uma letra.")
        if not letra_digitada.isalpha():
            print("Por favor, digite apenas letras do alfabeto.")
        letra_digitada = input("Digite uma letra: ").upper()

    os.system('cls' if os.name == 'nt' else 'clear')

    if letra_digitada in palavra_descoberta: # Letras repetidas não consomem tentativas.
        print("Você já descobriu essa letra.")
        continue
    else:
        tentativas += 1 
        
    print(f"Tentativa = {tentativas}") # Mostra a quantidade de tentativas que o usuário já fez
    if tentativas == tentativas_total - 1: # Caso o usuário esteja na penúltima tentativa, avisa que falta apenas uma tentativa
        print("Falta 1 tentativa!")

    if letra_digitada in palavra_secreta: # Verifica se a letra digitada está na palavra secreta
        palavra_descoberta += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta: # Monta a palavra formada até o momento, substituindo as letras não descobertas por "*"
        if letra_secreta in palavra_descoberta:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(f"Palavra formada até agora: {palavra_formada}") # imprime a palavra formada até o momento, com as letras descobertas e os "*" representando as letras não descobertas

    if palavra_formada == palavra_secreta: # Verifica se o usuário descobriu a palavra secreta
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela para que as tentativas anteriores não fiquem visíveis
        print(f"Parabéns! Você descobriu a palavra secreta '{palavra_secreta}' em {tentativas} tentativas.")
        break

    if tentativas == tentativas_total: # Verifica se o usuário atingiu o número máximo de tentativas
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você perdeu! Não conseguiu adivinha em {tentativas_total} tentativas ")
        print(f"A palavra secreta era: '{palavra_secreta}'")
        break

