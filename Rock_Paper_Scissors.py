import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move_ = my_move
        self.their_move_ = their_move
        return

    def __init__(self):
        self.score = 0
        self.my_move_ = random.choice(moves)
        self.their_move_ = random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move_


class CyclePlayer(Player):
    def move(self):
        if self.my_move_ == 'rock':
            return 'paper'
        elif self.my_move_ == 'paper':
            return 'scissors'
        else:
            return 'rock'


def PlayGames():
    Games = input('You want play random or reflect or cycler?').lower()
    if Games == 'random':
        return Game(HumanPlayer(), RandomPlayer())
    elif Games == 'reflect':
        return Game(HumanPlayer(), ReflectPlayer())
    elif Games == 'cycler':
        return Game(HumanPlayer(), CyclePlayer())
    else:
        print('Please Correct!')
        return PlayGames()


class HumanPlayer(Player):
    def move(self):
        user = input('You want start rock or paper or scissors ?').lower()
        if user == 'q':
            exit()
        elif user in moves:
            return user
        else:
            print('Please Correct!')
            return self.move()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"human: {move1}  computer: {move2}")
        if beats(move1, move2):
            self.p1.score = self.p1.score + 1
            print('You win')
        elif beats(move2, move1):
            self.p2.score = self.p2.score + 1
            print('you lose!')
        print(f"scores: human: {self.p1.score}  computer: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print(f"scores: you: {self.p1.score}  computer: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("You Win")
        elif self.p1.score < self.p2.score:
            print("You Lose")


if __name__ == '__main__':
    game = PlayGames()
    game.play_game()
