#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class AlwaysRockPlayer(Player):
    def move(self):
        return 'rock'

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class ImitatePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_opponent_move = None

    def move(self):
        if self.last_opponent_move:
            return self.last_opponent_move
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move

class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.current_move = None

    def move(self):
        if self.current_move:
            self.current_move = moves[(moves.index(self.current_move) + 1) % 3]
        else:
            self.current_move = random.choice(moves)
        return self.current_move

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("Player 1 wins!")
            self.p1_score += 1
        else:
            print("Player 2 wins!")
            self.p2_score += 1

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"Player 1: {self.p1_score}, Player 2: {self.p2_score}")

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

if __name__ == '__main__':
    game = Game(AlwaysRockPlayer(), ImitatePlayer())
    game.play_game()
