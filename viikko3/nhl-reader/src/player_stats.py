class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        scorers = list(filter(lambda player: player.nationality == nationality,
                              sorted(players, key=lambda player: player.goals + player.assists,
                                     reverse=True)))
        return scorers
