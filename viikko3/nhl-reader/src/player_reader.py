import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
      url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
      response = requests.get(url).json()
      self.players = []
      for player_dict in response:
          self.players.append(Player(player_dict))