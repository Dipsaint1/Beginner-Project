from Tic_Tac_Toe import Game
from First_Player_Tic_Tac_Toe import PlayerOne
from Second_Player_Tic_Tac_Toe import PlayerTwo


class Menu:
    def __init__(self):
        super().__init__()
        self.player_1 = PlayerOne()  # Initialize player_1 contact class
        self.player_2 = PlayerTwo()  # Initialize player_2 contact class
        self.game = Game()

    def run(self):
        counter = 0
        board = self.game.create_initial_board()
        print()
        self.game.show_board(board)

        while True:
            # Player 1 turn
            while True:
                move = self.player_1.play()
                if board[move] == "X" or board[move] == "O":
                    print("Invalid move, choose another block")     # Ensure player enters the correct input else, try again
                else:
                    board[move] = "X"
                    self.game.show_board(board)
                    counter += 1
                    break
            if counter >= 3 and self.player_1.player_1_wins(board):
                print(f"\n{self.player_1.name} WINS")
                break

            if counter == 5 and not self.player_1.player_1_wins(board) and not self.player_2.player_2_wins(board):
                print("TIE")
                break

            # Player 2 is the next to play
            while True:
                # player 2 turn
                move = self.player_2.play()
                if board[move] == "X" or board[move] == "O":    # Ensure player enters the correct input else, try again
                    print("Invalid move, choose another block")
                else:
                    board[move] = "O"
                    self.game.show_board(board)
                    break

            if counter >= 2 and self.player_2.player_2_wins(board):
                print(f"\n{self.player_2.name} WINS")
                break


if __name__ == "__main__":
    Menu().run()