import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your tokens
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
NEWSDATA_API_URL = "https://newsdata.io/api/1/news?apikey=pub_688017fca8c049520b4d9f519c561ec08478a&q=Sri%20lanka%20helakuru%20news"

# Function to fetch news
def get_news():
    response = requests.get(NEWSDATA_API_URL)
    data = response.json()
    
    if "results" in data:
        news_list = data["results"][:5]  # Get top 5 news articles
        news_text = ""
        for news in news_list:
            title = news.get("title", "No Title")
            link = news.get("link", "#")
            news_text += f"🔹 {title}\n🔗 {link}\n\n"
        return news_text
    return "No news found."

# Command handler for /news
def news(update: Update, context: CallbackContext) -> None:
    news_text = get_news()
    update.message.reply_text(news_text)

# Main function to run the bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("news", news))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
