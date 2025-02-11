import requests
import config
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

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
async def news(update: Update, context: CallbackContext):
    news_text = get_news()
    await update.message.reply_text(news_text)

# Main function to run the bot
def main():
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("news", news))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()