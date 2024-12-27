import os
import logging
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools
from phi.tools.youtube_tools import YouTubeTools
from config import *

# Load environment variables
load_dotenv()


finance_agent = Agent(
    model=Gemini(id="gemini-1.5-flash-8b"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True
    )],
    # show_tool_calls=True,
    markdown=True,
    instructions=['Use tables to display the data'],
)

youtube_agent = Agent(
    model=Gemini(id="gemini-1.5-flash-8b"),
    tools=[YouTubeTools(
        
    )],
    # show_tool_calls=True,
    markdown=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    instructions=[''],
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_MESSAGE)

async def stock_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(INVALID_STOCK_SYMBOL)
        return

    symbol = context.args[0].upper()
    status_message = await update.message.reply_text(ANALYZING_STATUS.format(symbol))
    
    try:
        response = finance_agent.run(
            STOCK_ANALYSIS_PROMPT.format(symbol=symbol),
            stream=False
        ).content

        response_text = STOCK_RESPONSE_TEMPLATE.format(symbol, str(response))
        await status_message.delete()
        
        await update.message.reply_text(
            response_text,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logging.error(f"Error in stock_command: {str(e)}")
        await status_message.delete()
        await update.message.reply_text(GENERIC_ERROR.format(symbol))

async def compare_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text(INVALID_COMPARE_SYMBOLS)
        return

    symbol1 = context.args[0].upper()
    symbol2 = context.args[1].upper()
    status_message = await update.message.reply_text(COMPARING_STATUS.format(symbol1, symbol2))
    
    try:
        response = finance_agent.run(
            STOCK_COMPARISON_PROMPT.format(symbol1=symbol1, symbol2=symbol2),
            stream=False
        ).content
        
        response_text = COMPARISON_RESPONSE_TEMPLATE.format(symbol1, symbol2, str(response))
        await status_message.delete()
        
        await update.message.reply_text(
            response_text,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logging.error(f"Error in compare_command: {str(e)}")
        await status_message.delete()
        await update.message.reply_text(COMPARE_ERROR)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(INVALID_COMMAND)

async def youtube_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the youtube command."""
    # Check if we have enough arguments
    if not context.args or len(context.args) < 2:
        await update.message.reply_text(INVALID_YOUTUBE_COMMAND)
        return

    # Extract URL and question
    video_url = context.args[0]
    question = ' '.join(context.args[1:])

    # Validate URL (basic check)
    if not ('youtube.com' in video_url or 'youtu.be' in video_url):
        await update.message.reply_text("Please provide a valid YouTube URL.")
        return

    status_message = await update.message.reply_text(YOUTUBE_ANALYZING)
    
    try:
        response = youtube_agent.run(
            YOUTUBE_PROMPT.format(question=question, url=video_url),
            stream=False
        ).content

        print(response)

        # Format the response
        response_text = YOUTUBE_RESPONSE_TEMPLATE.format(
            question=question,
            response=str(response),
            url=video_url
        )

        # Delete status message
        await status_message.delete()
        
        # Send response
        await update.message.reply_text(
            response_text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=False  # Allow video thumbnail preview
        )
        
    except Exception as e:
        logging.error(f"Error in youtube_command: {str(e)}")
        await status_message.delete()
        await update.message.reply_text(YOUTUBE_ERROR)

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stock", stock_command))
    application.add_handler(CommandHandler("compare", compare_command))
    application.add_handler(CommandHandler("youtube", youtube_command))
    
    # Add message handler for other messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()