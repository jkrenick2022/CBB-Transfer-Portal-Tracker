import requests
import dotenv
import os
from models import Player

dotenv.load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
PORTAL_ROLE_ID = os.getenv('PORTAL_ROLE_ID')

def send_discord_alert(player: Player, status: str):
    if status == "new":
        title = "📥 New Transfer Portal Entry"
        color = 0x1ABC9C
    elif status == "updated":
        title = "✅ Player Committed"
        color = 0x2ECC71

    embed = {
    "title": title,
    "color": color,
    "fields": [
        {"name": "Player", "value": f"**{player.name}** ({player.class_year})", "inline": False},
        {"name": "Height", "value": player.height or "N/A", "inline": True},
        {"name": "Weight", "value": player.weight or "N/A", "inline": True},
        {"name": "From", "value": player.previous_team or "Unknown", "inline": True},
        {"name": "To", "value": player.committed_team or "Undecided", "inline": True},
        {"name": "Portal Entry Date", "value": player.entry_date.strftime('%m/%d/%Y'), "inline": True}
    ],
    "thumbnail": {"url": player.profile_img_url or "https://cdn-icons-png.flaticon.com/512/149/149071.png"}
}

    payload = {
        "content": f"<@&{PORTAL_ROLE_ID}>",
        "embeds": [embed],
        "allowed_mentions": {
            "roles": [PORTAL_ROLE_ID]
        }
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code not in [200, 204]:
            print(f"❌ Discord alert failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Exception sending Discord alert: {e}")