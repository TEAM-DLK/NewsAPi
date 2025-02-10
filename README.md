📢 Telegram News Bot

A Telegram bot that fetches the latest Sri Lanka Helakuru news using the NewsData.io API and sends updates to users.

🚀 Features
	•	Fetches latest Sri Lanka news from NewsData.io.
	•	Uses Telegram Bot API to respond to /news command.
	•	Supports Heroku and Docker deployment.

🔧 Setup Instructions

1️⃣ Get API Keys
	1.	Create a Telegram Bot:
	•	Go to BotFather on Telegram.
	•	Use /newbot to create a bot and get the Telegram Bot Token.
	2.	Get NewsData API Key:
	•	Sign up at NewsData.io.
	•	Get your API Key from the dashboard.

2️⃣ Local Setup

🔹 Install Dependencies

pip install -r requirements.txt

🔹 Create config.py

Create a config.py file and add:

TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
NEWSDATA_API_KEY = "your_newsdata_api_key"

🔹 Run the Bot Locally

python news_bot.py

☁️ Deploy to Heroku

🔹 Using Heroku CLI

heroku login
heroku create your-bot-name
git push heroku main
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set NEWSDATA_API_KEY=your_api_key
heroku ps:scale worker=1
heroku restart

🔹 One-Click Deploy

Click the button below to deploy directly to Heroku:

🐳 Deploy with Docker

🔹 Build & Run Locally

docker build -t telegram-news-bot .
docker run --env TELEGRAM_BOT_TOKEN=your_token --env NEWSDATA_API_KEY=your_api_key telegram-news-bot

🔹 Deploy to Heroku

heroku container:login
heroku container:push web -a your-bot-name
heroku container:release web -a your-bot-name
heroku ps:scale web=1

🛠 Bot Commands

Command	Description
/news	Fetches the latest Sri Lanka Helakuru news

📜 License

This project is licensed under the MIT License.
