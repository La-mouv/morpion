class Morpion:
    def __init__(self):
        self.board = [' '] * 9
        self.current_symbol = 'X'

    def draw_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i+1], '|', self.board[i+2])
            if i < 6:
                print('---------')

    def change_player(self):
        self.current_symbol = 'O' if self.current_symbol == 'X' else 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_symbol
            if self.check_win():
                self.draw_board()
                print(self.current_symbol, "a gagné!")
                return True
            if ' ' not in self.board:
                self.draw_board()
                print("Match nul!")
                return True
            self.change_player()
            return False
        else:
            print("Position déjà prise!")
            return False

    def check_win(self):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for comb in win_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] != ' ':
                return True
        return False

    def start_game(self):
        while True:
            self.draw_board()
            position = int(input(f"{self.current_symbol}, choisissez une position (0-8): "))
            if position < 0 or position > 8:
                print("Position invalide!")
                continue
            if self.make_move(position):
                break

if __name__ == "__main__":
    game = Morpion()
    game.start_game()
