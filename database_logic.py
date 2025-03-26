import sqlite3
from models import Player

class DatabaseManager:
    def __init__(self, db_name="transfer_portal.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except Exception as e:
            print('Error occured: ', e)

    def create_table(self):
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS portal_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    class_year TEXT NOT NULL,
                    height TEXT NOT NULL,
                    weight TEXT NOT NULL,
                    portal_entry_date DATE NOT NULL,
                    previous_team TEXT NOT NULL,
                    committed_team TEXT NOT NULL,
                    img_url TEXT NOT NULL
                )
            """
        )
        self.conn.commit()

    def check_existing_player(self, player_name: str):
        self.cursor.execute(
            """
                SELECT * FROM portal_entries WHERE name = ?
            """, (player_name,)
        )
        return self.cursor.fetchone()

    def add_player(self, player: Player):
        try:
            self.cursor.execute(
                """
                    INSERT INTO portal_entries (
                        name, class_year, height, weight, portal_entry_date, previous_team, committed_team, img_url
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (player.name, player.class_year, player.height, player.weight, player.entry_date, player.previous_team,
                        player.committed_team, player.profile_img_url)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Integrity Error: {e}")
            return False
        except Exception as e:
            print(f"Error adding player: {e}")
            return False

    def update_player(self, player: Player):
        try:
            self.cursor.execute(
                """
                    UPDATE portal_entries
                    SET committed_team = ?
                    WHERE name = ?
                """, (player.committed_team, player.name)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error udpating player: {e}")
            return False
        
    def delete_table(self):
        self.cursor.execute(
            """
                DROP TABLE portal_entries
            """
        )
        self.conn.commit()