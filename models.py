from dataclasses import dataclass
from datetime import date

@dataclass
class Player:
    name: str
    class_year: str
    height: str
    weight: str
    entry_date: date
    previous_team: str
    committed_team: str
    profile_img_url: str