import logging
import requests
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN, NEWSDATA_API_KEY

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# NewsData.io API URL
NEWSDATA_API_URL = "https://newsdata.io/api/1/news"

# Function to fetch news from NewsData.io
def get_news():
    params = {
        "apikey": NEWSDATA_API_KEY,
        "q": "Sri Lanka helakuru news",  # Modify as needed
        "language": "en",  # Ensure it's fetching English news
    }

    try:
        response = requests.get(NEWSDATA_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Debugging: Print the API response
        logger.info(f"API Response: {data}")

        if "results" in data and data["results"]:
            news_list = data["results"][:5]  # Get top 5 news
            news_text = "\n\n".join([f"🔹 {n['title']}\n🔗 {n['link']}" for n in news_list])
            return news_text
        else:
            return "No news found for the given query."

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching news: {e}")
        return "Error fetching news. Please try again later."

# Command handler for "/news"
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    news_text = get_news()
    await update.message.reply_text(news_text)

# Main function to start the bot
async def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("news", news))

    # Start the bot using long polling
    await application.run_polling()

if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # If no event loop is running, create a new one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    else:
        # If an event loop is already running, run the bot within it
        loop.create_task(main())
        loop.run_forever()