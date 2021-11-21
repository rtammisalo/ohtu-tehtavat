import time
import requests
from player import Player


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)

        players.append(player)

    print(f'Players from FIN {time.asctime()}:\n')

    for player in filter(lambda player: player.nationality == 'FIN',
                         sorted(players, key=lambda player: player.goals + player.assists,
                                reverse=True)):
        print(player)


if __name__ == "__main__":
    main()
