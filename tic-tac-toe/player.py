import math, random, time

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        square = None
        while not valid_square: 
            square = input(self.letter +'\'s turn. Input move (0-8): ')
            try:
                square = int(square)
                if square not in game.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input try again!')
                time.sleep(0.8)
        return square
    
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return super().get_move(game)

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_move())


class MediumComuterPlayer(ComputerPlayer):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = game.available_move()
        for i in move:
            right_move = game.winner(i, self.letter)
            if right_move:
                print(i)
                return i
        return random.choice(move)    

class SuperComputerPlayer(ComputerPlayer):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if (len(game.available_move()) == 9):
           square = random.choice(game.available_move())
           return square
        else:
           square = self.minmax(game, self.letter)['position'] 
           return square
        
    def minmax(self, state, player):
        max_player = self.letter #yourself 
        other_player = 'o' if player == 'x' else 'x'

        # This is base case's
        if state.current_winner == other_player:
            return {'position': None, "score": 1*(state.num_empty_square() +1) if other_player == max_player else -1*(state.num_empty_square() +1)}
        elif not state.empty_square():
            return {'position': None, "score": 0}
        
        if player == max_player:
            best = {'position': None, "score": -math.inf}
        else: 
            best = {'position': None, "score": math.inf}

        
        for posible_move in state.available_move():
            # step 1 make a move 
            state.make_move(posible_move, player)

            # step 2 recurce the minmax to simulate a game after making that move
            sim_score = self.minmax(state, other_player)     

            # step 3 undo the move
            state.board[posible_move] = ' '           
            state.current_winner= None
            sim_score['position'] = posible_move

            # stpe 4 update the best if necessary 
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best