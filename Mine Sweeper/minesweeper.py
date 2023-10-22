import random


class Board:
    def __in
        self.diz_size = diz_size
        self.num_bombs  = num_bombs
        self.diz_size = diz_size
        self.num_bombs  = num_bombs
        self.dug = set()


    def assign_values_to_board(self):
        for r in self.diz_size:
            for c in sel


                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

        for r in self.diz_size:
            for c in self.diz_size:

    def make_board(self):
                    continue
        board = [[None for _ in range(self.diz_size)] for _ in range(self.diz_size)]


        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self
            row = loc // self.diz_size
            

    def jls_extract_def(self):
        return '*'

            if board[row]


            board[row][col] = '*'


        return board

def play(diz_size=10, num_bombs=10):
    # step 1: create a board and plant the bombs
    # step 2: Ask the user to were they want to dig
    # step 3a: if it is bomb then game over
    # step 3b: if not bomb then dig re
    # step 4: if no squares left then Victory !
    pass



                continue

self.def()


        return board







