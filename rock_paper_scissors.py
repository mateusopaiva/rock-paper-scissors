import random
from utils import clear_screen

class RockPaperScissorsGame:
    def __init__(self):
        self.move_list = ["Pedra", "Papel", "Tesoura"]
        self.player_count = 0
        self.computer_count = 0
        self.player_move = None
        self.computer_move = None
        self.winner = None

    def main_print(self):
        clear_screen()
        print("=========================================")
        print("\nPLACAR:")
        print(f"Você: {self.player_count}")
        print(f"Computador: {self.computer_count}")
        print("\n")
        print("Escolha uma jogada:")
        print("0 - Pedra | 1 - Papel | 2 - Tesoura")

    def get_player_move(self):
        while True:
            try:
                player_move = int(input())
                if player_move not in [0, 1, 2]:
                    raise ValueError("Escolha inválida. Escolha 0, 1 ou 2.")
                self.player_move = self.move_list[player_move]
                return self.player_move
            except ValueError as e:
                print(e)

    def select_move(self):
        self.computer_move = random.choice(self.move_list)
        return self.computer_move

    def select_winner(self):
        outcomes = {
            ("Papel", "Pedra"): "Player",
            ("Papel", "Tesoura"): "Computer",
            ("Pedra", "Tesoura"): "Player",
            ("Pedra", "Papel"): "Computer",
            ("Tesoura", "Papel"): "Player",
            ("Tesoura", "Pedra"): "Computer",
        }
        
        if self.player_move == self.computer_move:
            self.winner = "Draw"
        else:
            result = outcomes.get((self.player_move, self.computer_move))
            if result == "Player":
                self.player_count += 1
            elif result == "Computer":
                self.computer_count += 1
            self.winner = result

        print("===========================")
        print(f"Sua jogada: {self.player_move.upper()}")
        print(f"Jogada do computador: {self.computer_move.upper()}")

        if self.winner == "Player":
            print("Você venceu!")
        elif self.winner == "Computer":
            print("Você perdeu!")
        else:
            print("Empate!")

        print("===========================")

    def play_again(self):
        while True:
            print("\nJogar novamente? 0 - NÃO | 1 - SIM")
            try:
                next_move = int(input())
                if next_move == 0:
                    print("Obrigado por jogar!")
                    return False
                elif next_move == 1:
                    return True
                else:
                    print("Escolha inválida. Escolha 0 ou 1.")
            except ValueError:
                print("Escolha inválida. Digite 0 ou 1.")