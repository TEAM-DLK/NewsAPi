import requests
import os

# Try to import local config (for local development)
try:
    import config
    TELEGRAM_BOT_TOKEN = config.TELEGRAM_BOT_TOKEN
    NEWSDATA_API_KEY = config.NEWSDATA_API_KEY
except ImportError:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

# News API URL
NEWSDATA_API_URL = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_API_KEY}&q=Sri%20lanka%20helakuru%20news"

def get_news():
    response = requests.get(NEWSDATA_API_URL)
    data = response.json()
    if "results" in data:
        news_list = data["results"][:5]
        news_text = "\n\n".join([f"🔹 {n['title']}\n🔗 {n['link']}" for n in news_list])
        return news_text or "No news found."
    return "Error fetching news."

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def news(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(get_news())

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("news", news))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()