from player import Player


class TennisGame:
    POINTS_TO_SCORE = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    MINIMUM_GAME_POINT = 4
    TIE_BREAKER = 2

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if self.player1.name == player_name:
            self.player1.won_point()
        else:
            self.player2.won_point()

    def _get_tie_score(self):
        if self.player1.points in self.POINTS_TO_SCORE:
            return f"{self.POINTS_TO_SCORE[self.player1.points]}-All"
        return "Deuce"

    def _get_victory_score(self):
        player = self._get_winning_player()
        return f"Win for {player.name}"

    def _get_advantage_score(self):
        if self.player1.points > self.player2.points:
            player = self.player1
        else:
            player = self.player2
        return f"Advantage {player.name}"

    def _get_normal_score(self):
        player1_score = self.POINTS_TO_SCORE[self.player1.points]
        player2_score = self.POINTS_TO_SCORE[self.player2.points]
        return f"{player1_score}-{player2_score}"

    def _is_game_over(self):
        point_difference = abs(self.player1.points - self.player2.points)
        if point_difference >= self.TIE_BREAKER:
            return True
        return False

    def _get_winning_player(self):
        if self.player1.points > self.player2.points:
            return self.player1
        return self.player2

    def _is_tie(self):
        return self.player1.points == self.player2.points

    def _is_game_point_impossible(self):
        max_points = max(self.player1.points, self.player2.points)
        return max_points < self.MINIMUM_GAME_POINT

    def get_score(self):
        if self._is_tie():
            return self._get_tie_score()

        if self._is_game_point_impossible():
            return self._get_normal_score()

        if self._is_game_over():
            return self._get_victory_score()

        return self._get_advantage_score()
