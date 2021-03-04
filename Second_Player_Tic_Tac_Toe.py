from Tic_Tac_Toe import Game, display_initial_board


class PlayerTwo(Game):
    def __init__(self):
        super().__init__()
        while True:
            name = input("Player 2 name: ").upper()
            name = name.lstrip()
            name = name.rstrip()
            if name.isalpha():
                break
            else:
                print("Name should contain only alphabets!")
        self.name = name

    def play(self):
        while True:
            move = input(f"\nO = {self.name}'s turn, move to which block: ")
            if move in self.moves:
                if move == "1":
                    return move

                elif move == "2":
                    return move

                elif move == "3":
                    return move

                elif move == "4":
                    return move

                elif move == "5":
                    return move

                elif move == "6":
                    return move

                elif move == "7":
                    return move

                elif move == "8":
                    return move

                elif move == "9":
                    return move
            else:
                print("Invalid input")
                display_initial_board()

    def player_2_wins(self, board):
        if (board["1"] == board["2"] == board["3"] == "O") or (board["1"] == board["4"] == board["7"] == "O")\
             or (board["1"] == board["5"] == board["9"] == "O") or (board["2"] == board["5"] == board["8"] == "O")\
             or (board["4"] == board["5"] == board["6"] == "O") or (board["3"] == board["6"] == board["9"] == "O")\
             or (board["7"] == board["8"] == board["9"] == "O") or (board["3"] == board["5"] == board["7"] == "O"):
            return True

        return False

