class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            return self._get_by_score(self.score1, all=True)

        if max(self.score1, self.score2) < 4:
            return f"{self._get_by_score(self.score1)}-{self._get_by_score(self.score2)}"

        return self._get_by_diff()

    
    def _get_by_score(self, id, all=None):
        array = ["Love", "Fifteen", "Thirty", "Forty"]
        if id > 3:
            return "Deuce"
        return array[id] if all is None else f"{array[id]}-All"
    
    def _get_by_diff(self):
        score_diff = self.score1 - self.score2
        ahead_player = self.player1 if score_diff > 0 else self.player2
        if abs(score_diff) == 1:
            return f"Advantage {ahead_player}"
        return f"Win for {ahead_player}"
