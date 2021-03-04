import datetime


def display_initial_board():
    board = {"1": "1", "2": "2", "3": "3",
             "4": "4", "5": "5", "6": "6",
             "7": "7", "8": "8", "9": "9"
            }

    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])


class Game:
    def __init__(self):
        self.date_created = datetime.datetime.today()
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def create_initial_board(self):
        initial_board = {"1": "-", "2": "-", "3": "-",
                         "4": "-", "5": "-", "6": "-",
                         "7": "-", "8": "-", "9": "-"
                         }
        return initial_board

    def show_board(self, board):
        print(board["1"] + "|" + board["2"] + "|" + board["3"])
        print("-+-+-")
        print(board["4"] + "|" + board["5"] + "|" + board["6"])
        print("-+-+-")
        print(board["7"] + "|" + board["8"] + "|" + board["9"])



