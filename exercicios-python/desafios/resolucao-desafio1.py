# Pseudocódigo

"""
Solicitar entrada Jogador1
Solicitar entrada Jogador2

Verificar se as opções desejadas estão dentro das permitidas.

Condicionais:

-Pedra vence a Tesoura (quebrando-a).
-Tesoura vence o Papel (cortando-o).
-Papel vence a Pedra (cobrindo-a).
Se ambos os jogadores escolherem o mesmo objeto, a rodada resulta em um empate.

"""

print ("Bem-vindo ao jogo, escolha Pedra, Papel ou Tesoura, as regras são as seguintes: \n"
"-Pedra vence a Tesoura (quebrando-a).\n" 
"-Tesoura vence o Papel (cortando-o).\n" 
"-Papel vence a Pedra (cobrindo-a).\n" 
"Se ambos os jogadores escolherem o mesmo objeto, a rodada resulta em um empate.\n") 

# Solicita as entradas e verifica se a opção é válida

while True:

    # Solicita entradas dos jogadores e converte pra minúsculo pra verificar as condições

    jogador1 = input("Jogador 1, digite uma opção: ")
    opcao_jogador1 = jogador1.lower()
    jogador2 = input("Jogador 2, digite uma opção: ")
    opcao_jogador2 = jogador2.lower()

    opcoes = ["pedra", "papel", "tesoura"]

    if opcao_jogador1 in opcoes and opcao_jogador2 in opcoes:
        pass
    else:
        print("Opção inválida, digite novamente!")

# Verifica se há um vencedor ou empate

    if opcao_jogador1 == "pedra" and opcao_jogador2 == "tesoura":
        print("O Jogador 1 venceu!")

    elif opcao_jogador2 == "pedra" and opcao_jogador1 == "tesoura":
        print ( "O Jogador 2 venceu!")

    elif opcao_jogador1 == "tesoura" and opcao_jogador2 == "papel":
        print("O Jogador 1 venceu!")

    elif opcao_jogador2 == "tesoura" and opcao_jogador1 == "papel":
        print ( "O Jogador 2 venceu!")

    elif opcao_jogador1 == "papel" and opcao_jogador2 == "pedra":
        print("O Jogador 1 venceu!")

    elif opcao_jogador2 == "papel" and opcao_jogador1 == "pedra":
        print ( "O Jogador 2 venceu!")

    elif opcao_jogador1 == opcao_jogador2:
        print ("Empatou, joguem novamente!")

