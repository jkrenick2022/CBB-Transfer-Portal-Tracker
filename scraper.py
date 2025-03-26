from playwright.sync_api import sync_playwright
from datetime import datetime, date
from bs4 import BeautifulSoup
from models import Player

def get_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.on3.com/transfer-portal/wire/basketball/")

        for _ in range(10):
            try:
                page.click('text="Load More"')
                page.wait_for_timeout(1500)  # wait for new items to load
            except:
                break
        
        # Get HTML content
        html = page.content()
        browser.close()

        if html:
            print('page parssed')
        else:
            print('no data')

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(class_ = 'TransferPortalPage_transferPortalList__vbYpa')
    entries = table.find_all('li')

    players = []
    cutoff_date = date(2025, 3, 1)
    for player in entries:
        try:
            date_tag = player.find(class_="TransferPortalItem_statusDate__gnRV0")
            if not date_tag:
                continue

            raw_date = date_tag.get_text(strip=True)
            portal_entry_date = datetime.strptime(raw_date, "%m/%d/%Y").date()
            if portal_entry_date <= cutoff_date:
                continue

            img_tag = player.find("img")
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else "https://militaryhealthinstitute.org/wp-content/uploads/sites/37/2021/08/blank-profile-picture-png.png"

            name_tag = player.find(class_="TransferPortalItem_playerNameContainer__bwhKH")
            name = name_tag.find('a').get_text(strip=True) if name_tag else "Unknown"

            year_tag = player.find(class_="TransferPortalItem_classYear__JDxgx")
            year = year_tag.get_text(strip=True) if year_tag and len(year_tag.get_text(strip=True)) > 1 else "N/A"
            
            height_tag = player.find(class_="TransferPortalItem_height__6VhrL")
            height = height_tag.get_text(strip=True) if height_tag and len(height_tag.get_text(strip=True)) > 1 else "N/A"

            weight_tag = player.find(class_="TransferPortalItem_weight__K0dN2")
            weight = weight_tag.get_text(strip=True) if weight_tag and len(weight_tag.get_text(strip=True)) > 1 else "N/A"

            team_logos = player.find_all("img", class_="TransferPortalItem_teamLogo___on5w")
            prev_team = team_logos[0]["title"] if len(team_logos) >= 1 else "Unknown"
            dest_team = team_logos[1]["title"] if len(team_logos) >= 2 else "Undecided"

            player = Player(
                name = name,
                class_year = year,
                height = height,
                weight = weight,
                entry_date = portal_entry_date,
                previous_team = prev_team,
                committed_team = dest_team,
                profile_img_url = img_url
            )

            players.append(player)
        except Exception as e:
            print(f"Failed to parse a player: {e}")

    print('All players scraped')
    return players

