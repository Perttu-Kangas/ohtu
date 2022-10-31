import unittest
from statistics import Statistics
from player import Player
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):

    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
      player = self.statistics.search("Semenko")
      self.assertEqual(player.name, "Semenko")
      self.assertEqual(player.team, "EDM")
      self.assertEqual(player.goals, 4)
      self.assertEqual(player.assists, 12)

    def test_search_not_found(self):
      self.assertEqual(self.statistics.search("asd"), None)

    def test_search_team(self):
      players = self.statistics.team("EDM")
      self.assertEqual(players[0].name, "Semenko")
      self.assertEqual(players[1].name, "Kurri")
      self.assertEqual(players[2].name, "Gretzky")
    
    def test_top(self):
      top_players = self.statistics.top(3)
      self.assertEqual(top_players[0].name, "Gretzky")
      self.assertEqual(top_players[1].name, "Lemieux")
      self.assertEqual(top_players[2].name, "Yzerman")
      self.assertEqual(len(top_players), 3)

    def test_top_by_goals(self):
      top_players = self.statistics.top(3, SortBy.GOALS)
      self.assertEqual(top_players[0].name, "Lemieux")
      self.assertEqual(top_players[1].name, "Yzerman")
      self.assertEqual(top_players[2].name, "Kurri")

    def test_top_by_assists(self):
      top_players = self.statistics.top(3, SortBy.ASSISTS)
      self.assertEqual(top_players[0].name, "Gretzky")
      self.assertEqual(top_players[1].name, "Yzerman")
      self.assertEqual(top_players[2].name, "Lemieux")