def sort_by_goals_plus_assists(player):
    return player.assists + player.goals

class PlayerStats:
    def __init__(self, player_reader):
      self.player_reader = player_reader
      self.player_reader.players.sort(
        reverse=True,
        key=sort_by_goals_plus_assists
    )

    def top_scorers_by_nationality(self, nationality):
      return filter(lambda p: (p.nationality == nationality), self.player_reader.players)
