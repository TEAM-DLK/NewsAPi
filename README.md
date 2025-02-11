📰 Telegram News Bot (Sri Lanka)

A Telegram bot that fetches the latest Sri Lankan news using NewsAPI and responds to the /news command.

📌 Features

✅ Fetches top news from NewsAPI
✅ Supports /news command to get the latest headlines
✅ Uses python-telegram-bot for Telegram API integration
✅ Supports deployment on Heroku (with or without Docker)

🚀 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/TEAM-DLK/NewsAPi.git
cd NewsAPi

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure API Keys

Create a config.py file and add your Telegram Bot Token and NewsAPI Key:

# config.py
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
NEWS_API_KEY = "your-news-api-key"

4️⃣ Run the Bot Locally

python news_bot.py

🛠 Deploying to Heroku

A. Deploy Without Docker
	1.	Login to Heroku:

heroku login


	2.	Create a new Heroku app:

heroku create your-app-name


	3.	Add a Procfile (if not already created):

worker: python news_bot.py


	4.	Deploy to Heroku:

git add .
git commit -m "Deploy Telegram bot to Heroku"
git push heroku main


	5.	Scale the worker:

heroku ps:scale worker=1



B. Deploy With Docker
	1.	Login to Heroku container registry:

heroku container:login


	2.	Build and push the Docker image:

heroku container:push web -a your-app-name


	3.	Release the container:

heroku container:release web -a your-app-name

📜 Usage
	•	Start a chat with your bot on Telegram
	•	Send /news to get the latest Sri Lankan news

🔧 Troubleshooting

Issue: telegram.error.BadRequest: Message text is empty
✔️ Fix: Ensure get_news() always returns text. Modify the function like this:

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=lk&apiKey={config.NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()

    if news_data.get("status") == "ok":
        articles = news_data.get("articles", [])
        if not articles:
            return "📰 No news available at the moment."
        
        news_list = [f"📰 {article['title']} - {article['url']}" for article in articles[:5]]
        return "\n\n".join(news_list)

    return "❌ Failed to fetch news."

📜 License

This project is open-source and licensed under the MIT License.

💡 Contributing

Feel free to submit pull requests or open issues for feature suggestions.
