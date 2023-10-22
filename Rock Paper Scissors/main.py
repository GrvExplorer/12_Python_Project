import random

# score_player = 0
# score_computer = 0

def play():
    user = input('p for paper, r for rock, s for scissors: ').lower()[0]
    print()
    computer = random.choice(['p', 's', 'r'])

    if (user == computer):
        return f'It\'s a tie computer choice {computer}'

    if is_wins(user, computer):
        # score_player += 1
        return f'You Won! computer choice {computer}'

    # score_computer += 1
    return f'You Lose! computer choice {computer}'

def is_wins(player, opponent):
    # p > r > s > p
    if ((player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')):
        return True

rounds = 1
while rounds < 4:
    print(play())
    # if (score_player > score_computer):
    #     print(f'U Won the match Your score = {score_player} Computer\'s score = {score_computer}')
    #     break
    # elif (score_computer > score_player):
    #     print(f'Game over! Comuter won Your score = {score_player} Computer\'s score = {score_computer}')

    rounds += 1