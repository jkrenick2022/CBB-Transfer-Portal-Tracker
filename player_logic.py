from database_logic import DatabaseManager
from scraper import get_data
from models import Player

class PlayerHandler:
    def __init__(self):
        self.db = DatabaseManager()
        self.players = get_data()

    def process_player(self, player: Player):
        existing_player = self.db.check_existing_player(player.name)

        if not existing_player:
            status = self.db.add_player(player)
            if status:
                return player, "new"
        
        player_committed_status = existing_player[7]
        if player_committed_status != player.committed_team:
            status = self.db.update_player(player)
            if status:
                return player, "updated"
            
        return player, "unchanged"
    
    def reset_players(self):
        self.players = get_data()