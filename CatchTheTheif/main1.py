from abc import ABC, abstractmethod
import getpass

player_names = ["P1", "P2", "P3", "P4"]

class IPlayer(ABC):
    @abstractmethod
    def pick_role(self) -> str:
        pass

class IScore(ABC):
    @abstractmethod
    def display_scores(self, players: list) -> None:
        pass

class Player(IPlayer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.role = None

    def pick_role(self) -> str:
        return self.role

    def set_role(self, role: str) -> None:
        self.role = role

class Score(IScore):
    def __init__(self) -> None:
        self.scores = {"P1": 0, "P2": 0, "P3": 0, "P4": 0}

    def update_score(self, player_name: str, score: int) -> None:
        if player_name in self.scores:
            self.scores[player_name] += score
        else:
            self.scores[player_name] = score

    def display_scores(self) -> None:
        print("\nCurrent Scores:")
        for player_name, score in self.scores.items():
            print(f"{player_name}: {score}")

    def get_winner(self) -> str:
        max_score = max(self.scores.values())
        winners = [p for p, score in self.scores.items() if score == max_score]
        return ', '.join(winners) if len(winners) > 1 else winners[0]

class CatchTheThief:
    def __init__(self, players: list, score: IScore) -> None:
        self.players = players
        self.score = score
        self.roles = {1: "King", 2: "Minister", 3: "Soldier", 4: "Thief"}
        self.points = {"King": 1000, "Minister": 500, "Soldier": 250, "Thief": 0}
        self.max_rounds = 3

    def assign_roles(self) -> None:
        assigned_roles = set()
        for p in self.players:
            while True:
                try:
                    role_no = int(getpass.getpass(f"{p.name}, enter your role (1 for King, 2 for Minister, 3 for Soldier, 4 for Thief): "))
                    if role_no in self.roles and role_no not in assigned_roles:
                        p.set_role(self.roles[role_no])
                        assigned_roles.add(role_no)
                        break
                    else:
                        print("Invalid role or role already taken. Please choose a different role.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")

    def play_round(self) -> None:
        self.assign_roles()

        king = next(p for p in self.players if p.role == "King")
        minister = next(p for p in self.players if p.role == "Minister")
        soldier = next(p for p in self.players if p.role == "Soldier")
        thief = next(p for p in self.players if p.role == "Thief")

        print(f"\n{king.name} (King): Minister, identify the Thief among Soldier and Thief.")
        guess_choices = [soldier.name, thief.name]
        print(f"{minister.name} (Minister), choose between {guess_choices[0]} and {guess_choices[1]}.")

        guess = input(f"{minister.name} (Minister), in my opinion the Thief is: ")

        if guess.capitalize() == thief.name:
            self.score.update_score(minister.name, self.points["Minister"])
            print(f"\nCorrect! {minister.name} guessed the Thief and gets {self.points['Minister']} points!")
        else:
            self.score.update_score(thief.name, 500)
            print(f"\nIncorrect! {thief.name} remains undiscovered and gets 500 points.")

        self.score.update_score(king.name, self.points["King"])
        self.score.update_score(soldier.name, self.points["Soldier"])

        self.score.display_scores()

    def play_game(self) -> None:
        print("Welcome to the Role Guessing Game!")

        for round_number in range(1, self.max_rounds + 1):  
            print(f"\n--- Round {round_number} ---")
            self.play_round()

        print("\nGame Over!")
        winner = self.score.get_winner()
        print("\nFinal Scores:")
        self.score.display_scores()
        print(f"\nThe winner is: {winner}")

if __name__ == "__main__":
    players = [Player(name) for name in player_names]

    score = Score()
    game = CatchTheThief(players, score)
    game.play_game()
