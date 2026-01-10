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

    opcao_jogador1 = input("Jogador 1, digite uma opção: ")
    opcao_jogador2 = input("Jogador 2, digite uma opção: ")
    opcoes = ["Pedra", "Papel", "Tesoura"]

    if opcao_jogador1 in opcoes and opcao_jogador2 in opcoes:
        continue
    else:
        print("Opção inválida, digite novamente!")







     

