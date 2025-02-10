import logging
import requests
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Your NewsData.io API URL and token
NEWSDATA_API_URL = "https://newsdata.io/api/1/news"
NEWSDATA_API_KEY = "pub_688017fca8c049520b4d9f519c561ec08478a"  # Replace with your API key

# Function to get news from NewsData.io
def get_news():
    # Construct the API URL
    params = {
        'apikey': NEWSDATA_API_KEY,
        'q': 'Sri Lanka helakuru news',  # You can modify the query as needed
    }
    
    try:
        response = requests.get(NEWSDATA_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Parse the news data
        if "results" in data:
            news_list = data["results"][:5]  # Get top 5 news
            news_text = "\n\n".join([f"🔹 {n['title']}\n🔗 {n['link']}" for n in news_list])
            return news_text or "No news found."
        else:
            return "No news found."
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching news: {e}")
        return "Error fetching news."

# Command handler function for '/news'
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    news_text = get_news()
    await update.message.reply_text(news_text)

# Main function to start the bot
def main() -> None:
    # Replace 'your_telegram_bot_token' with your bot's token
    TELEGRAM_BOT_TOKEN = "7306410200:AAH0EhPYB7ANk6bV4XIG63arhS-yAoHdIwQ"  # Replace with your Telegram bot token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add the /news command handler
    application.add_handler(CommandHandler("news", news))

    # Start the bot with long polling
    application.run_polling()

if __name__ == "__main__":
    try:
        # Check if an event loop is already running
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No event loop is running, so create a new one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    else:
        # An event loop is already running, so run the main function in it
        loop.create_task(main())
        loop.run_forever()