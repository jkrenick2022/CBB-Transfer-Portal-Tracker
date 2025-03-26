# 🏀 NCAA Transfer Portal Tracker Bot

This is an **automated NCAA basketball transfer portal tracker** built with Python, Playwright, SQLite, and GitHub Actions. It scrapes new player entries, detects updates (like commitments), and posts real-time alerts to a Discord server.

> Fully automated and runs **hourly** — no manual work required.

---

## ⚙️ Features

- 🧠 **Smart Player Tracking**: Detects new portal entries and commitment updates
- ⏱️ **Runs Every Hour** via GitHub Actions
- 🛠️ **Scrapes with Playwright** for full JavaScript page support
- 📦 **SQLite Database Persistence** using GitHub commits
- 🔔 **Discord Webhook Integration** for real-time alerts

---

## 📸 Discord Alert Preview

![Discord Embed Preview](https://i.imgur.com/ZdEjqfi.png)

<sub>(Sample embed with player name, stats, previous team, commitment, and profile image)</sub>

---

## 📁 Project Structure

<pre> . ├── main.py # Main script: entry point for scraping + DB logic ├── player_logic.py # Handles player check/add/update logic ├── notifier.py # Sends Discord embed messages ├── db.py # SQLite database handler ├── scraper.py # Scrapes player data from On3 ├── transfer_portal.db # Persisted database (committed after each run) ├── requirements.txt # Python dependencies └── .github/ └── workflows/ └── hourly.yml # GitHub Actions cron job (runs every hour) </pre>

---

## 🧠 How It Works

1. GitHub Actions triggers every hour
2. Script scrapes On3's transfer portal (using Playwright)
3. Compares scraped players to existing DB:
   - If new → adds to DB + sends Discord alert
   - If committed → updates DB + sends Discord alert
4. Commits the updated DB back to the repo (ensuring state is saved for next run)

---

## 🔧 Setup (for Personal Use)

> Want to run your own version of this tracker?

1. **Fork this repo**
2. Set these GitHub secrets under `Settings → Secrets → Actions`:
   - `DISCORD_WEBHOOK_URL`: your Discord webhook
   - `PORTAL_ROLE_ID`: the role ID to ping (optional)
3. (Optional) Modify `scraper.py` or `notifier.py` to customize data
4. GitHub Actions will run the bot every hour automatically

---

## 👨‍💻 Built With

- Python 🐍
- Playwright
- BeautifulSoup
- SQLite
- GitHub Actions
- Discord Webhooks

---

## 📣 Credits

Created by [Jon Krenick](https://github.com/jkrenick2022)  
Built for sports fans, data nerds, and Discord power users 💪
