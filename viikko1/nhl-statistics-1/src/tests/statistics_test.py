import unittest
from statistics import Statistics
from player import Player


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

    def test_init_sets_stub_players(self):
        kurri = self.statistics.search("Kurri")
        self.assertEqual(kurri.name, "Kurri")

    def test_search_finds_existing_player(self):
        self.assertIsNotNone(self.statistics.search("Gretzky"))

    def test_search_does_not_find_non_existing_player(self):
        self.assertIsNone(self.statistics.search("Huuhaa"))

    def test_team_returns_only_players_in_team(self):
        players = self.statistics.team("EDM")
        correct_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]
        self.assertEqual(len(players), len(correct_players))

        for correct_player in correct_players:
            found = False
            for player in players:
                if player.name == correct_player.name:
                    found = True
                    break
            self.assertTrue(found)

    def test_top_scorer_found_correctly(self):
        # metodi top_scorers antaa 2 pelaajaa how_many arvolla 1, miksi?
        top_players = self.statistics.top_scorers(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")
        
        # Alla oleva aiheuttaa IndexErrorin
        # self.statistics.top_scorers(1001)
