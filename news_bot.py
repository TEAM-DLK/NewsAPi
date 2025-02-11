import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import config  # Import config.py

# Function to fetch news
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=lk&apiKey={config.NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()
    
    if news_data.get("status") == "ok":
        articles = news_data.get("articles", [])
        news_list = [f"📰 {article['title']} - {article['url']}" for article in articles[:5]]
        return "\n\n".join(news_list)
    else:
        return "❌ Failed to fetch news."

# Command handler for /news
def news(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    news_text = get_news()
    context.bot.send_message(chat_id=chat_id, text=news_text)

# Main function to run the bot
def main():
    updater = Updater(config.TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("news", news))
    
    print("🤖 Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()