from player_logic import PlayerHandler
from notifier import send_discord_alert
import time


def run():
    handler = PlayerHandler()
    players = handler.players.copy()
    players = list(reversed(players))


    for player in players:
        player_obj, status = handler.process_player(player)

        if status == "new":
            print(f"[NEW] {player_obj.name}")
            send_discord_alert(player_obj, status)
            time.sleep(2)
        elif status == "updated":
            print(f"[UPDATED] {player_obj.name}")
            send_discord_alert(player_obj, status)
            time.sleep(2)
        else:
            print(f"[UNCHANGED] {player_obj.name}")


if __name__ == '__main__':
    run()