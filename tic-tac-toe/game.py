from player import HumanPlayer, ComputerPlayer, MediumComuterPlayer, SuperComputerPlayer
import math, os

class Tictactoe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    def available_move(self):
        return [num for num in range(9) if self.board[num] == ' ']
        # return [i for i,x in enumerate(self.board) if x == ' ']
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_game(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |' )

    @staticmethod
    def print_game_num():
        num_board = [[ str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |' )

    def empty_square(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')

    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]        
        if all([s == letter for s in row]):
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
            
        return False


    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

def play(game, x_player, o_player, print_game):
    letter = 'x'
    if print_game:
        game.print_game_num()
        print()
    while game.empty_square():
        move = None
        if letter == 'o':
            move = o_player.get_move(game)
        else:
            move = x_player.get_move(game)

        if game.make_move(move, letter):
            if print_game:
                print()
                os.system('cls')
                game.print_game_num()
                
            if print_game:
                print()
                print(letter + f'\'s make a move to square {move}')
                game.print_game()

            if game.current_winner:
                if print_game:
                    print(letter + '\'s win\'s!')
                return letter
        letter = 'o' if letter == 'x' else 'x'
    if print_game:
        print('Tie!')
        

if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    tie = 0  
    for i in range(100):
        x_player = SuperComputerPlayer('x')
        o_player = MediumComuterPlayer('o')
        t = Tictactoe()
        play(t, x_player, o_player, print_game=False)
        if t.current_winner == 'x':
            x_wins += 1
        elif t.current_winner == 'o':
            o_wins += 1
        else:
            tie += 1
    print(f'x = {x_wins} o = {o_wins} tie = {tie}')