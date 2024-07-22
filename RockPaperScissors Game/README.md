# RockPaperScissorsGame

The `RockPaperScissorsGame` is a simple implementation of the classic Rock-Paper-Scissors game. Players can play against each other or against the computer, and scores are tracked throughout the game.

## Class Definitions

### IPlayer (Interface)

```python
from abc import ABC, abstractmethod

class IPlayer(ABC):
    @abstractmethod
    def pick_move(self) -> str:
        pass
```
### IScore (Interface)
```python
from abc import ABC, abstractmethod

class IScore(ABC):
    @abstractmethod
    def display_scores(self) -> None:
        pass
```
### HumanPlayer
```python
class HumanPlayer(IPlayer):
    def pick_move(self) -> str:
        while True:
            choice = input("Enter your choice (rock, paper, scissors): ").lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
```
### ComputerPlayer
```python
import random

class ComputerPlayer(IPlayer):
    def pick_move(self) -> str:
        return random.choice(['rock', 'paper', 'scissors'])
```
### Score
```python
class Score(IScore):
    def __init__(self) -> None:
        self.player1_score = 0
        self.player2_score = 0

    def display_scores(self) -> None:
        print(f"\nPlayer 1 score: {self.player1_score}")
        print(f"Player 2 score: {self.player2_score}")
 ```
### RockPaperScissorsGame
```python
class RockPaperScissorsGame:
    def __init__(self, player1: IPlayer, player2: IPlayer, score: IScore) -> None:
        self.player1 = player1
        self.player2 = player2
        self.score = score

    def play_round(self) -> None:
        p1_choice = self.player1.pick_move()
        p2_choice = self.player2.pick_move()

        print(f"Player 1 chose: {p1_choice}")
        print(f"Player 2 chose: {p2_choice}")

        result = self.determine_winner(p1_choice, p2_choice)
        if result == 1:
            self.score.player1_score += 1
        elif result == -1:
            self.score.player2_score += 1

    def determine_winner(self, p1_choice: str, p2_choice: str) -> int:
        if p1_choice == p2_choice:
            print("It's a tie!")
            return 0
        elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
             (p1_choice == 'paper' and p2_choice == 'rock') or \
             (p1_choice == 'scissors' and p2_choice == 'paper'):
            print("Player 1 wins!")
            return 1
        else:
            print("Player 2 wins!")
            return -1

    def play_game(self) -> None:
        print("Welcome to Rock-Paper-Scissors!")

        while True:
            for a in range(1, 4):  
                print(f"\n--- New Round {a} ---")
                self.play_round()
                self.score.display_scores()

            play_again = input("\nDo you want to play another set of three rounds? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
```
## Usage
### Choose Opponent and Start the Game
```python
if __name__ == "__main__":
    print("Choose your opponent:")
    print("1. Another Player")
    print("2. Computer")

    opponent_choice = input("Enter 1 or 2: ")

    if opponent_choice == '1':
        player1 = HumanPlayer()
        player2 = HumanPlayer()
    elif opponent_choice == '2':
        player1 = HumanPlayer()
        player2 = ComputerPlayer()
    else:
        print("Invalid choice. Exiting the game.")
        exit()

    score = Score()
    game = RockPaperScissorsGame(player1, player2, score)
    game.play_game()
```
## How to Play
- **1.Choose Your Opponent:** You can either play against another human player or the computer.
- **2.Enter Your Move:** Each player (or the computer) will choose rock, paper, or scissors.
- **3.Determine Winner:** The game will determine the winner based on the classic rules:
    - Rock beats Scissors -
    - Scissors beats Paper
    - Paper beats Rock
- **4.Update and Display Scores**: Scores are updated and displayed after each round.
- **5.Play Again**: You have the option to play another set of three rounds or end the game.