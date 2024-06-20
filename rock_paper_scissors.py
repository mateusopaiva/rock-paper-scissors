import random
import os

move_list = ["Pedra", "Papel", "Tesoura"]
player_count = 0
computer_count = 0

print("=========================================")
print("Bem vindo ao jogo: Pedra, papel e tesoura")

def main_print():
    print("=========================================")
    print("\nPLACAR:")
    print(f"Você: {player_count}")
    print(f"Computador: {computer_count}")
    print("\n")
    print("Escolha uma jogada:")
    print("0 - Pedra | 1 - Papel | 2 - Tesoura")

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise ValueError("Escolha inválida. Escolha 0, 1 ou 2.")
            return move_list[player_move]
        except ValueError as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count

    if p_move == "Papel":
        if c_move == "Pedra":
            player_count += 1
            return "p"
        elif c_move == "Tesoura":
            computer_count += 1
            return "c"
        else:
            return "d"

    if p_move == "Pedra":
        if c_move == "Tesoura":
            player_count += 1
            return "p"
        elif c_move == "Papel":
            computer_count += 1
            return "c"
        else:
            return "d"

    if p_move == "Tesoura":
        if c_move == "Papel":
            player_count += 1
            return "p"
        elif c_move == "Pedra":
            computer_count += 1
            return "c"
        else:
            return "d"

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print("")
    print("===========================")
    print(f"Sua jogada: {player_move.upper()}")
    print(f"Jogada do computador: {computer_move.upper()}")

    if winner == "p":
        print("Você venceu!")
    elif winner == "c":
        print("Você perdeu!")
    else:
        print("Empate!")

    print("===========================")

    while True:
        print("\nJogar novamente? 0 - NÃO | 1 - SIM")
        next_move = int(input())
        if next_move == 1:
            break
        elif next_move == 0:
            again = 0
            break

    os.system("cls")
