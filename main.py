from rock_paper_scissors import RockPaperScissorsGame

def main():
    game = RockPaperScissorsGame()

    while True:
        game.main_print()
        game.get_player_move()
        game.select_move()
        game.select_winner()
        if not game.play_again():
            break

if __name__ == "__main__":
    main()
