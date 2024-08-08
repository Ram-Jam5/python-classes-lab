class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    def play_game(self):
        print("Welcome to python Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn
            self.check_for_winner()
            if not self.winner:
                self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.render()
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    def print_message(self):
        if self.tie:
            print("Tie Game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's {self.turn}'s turn!")
    def render(self):
        self.print_board()
        self.print_message()
    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                    return move
            else:
                print("Not a valid move. Space may be occupied or does not exist on the board. Enter a valid move (example: A1): ")  
    def check_for_winner(self):
        wins = [
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),
            ('a1', 'b2', 'c3'),
            ('a3', 'b2', 'c1'),
        ]
        for win in wins:
            if self.board[win[0]] and self.board[win[0]] == self.board[win[1]] == self.board[win[2]]:
                self.winner = self.board[win[0]]
                return
    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and self.winner is None:
            self.tie = True

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'


game_instance = Game()
game_instance.play_game()       