# Bot Messages
WELCOME_MESSAGE = """
Welcome to the Stock & Crypto Analysis Bot! 🚀

Available commands:
/start - Show this welcome message
/help - Show help message
/stock SYMBOL - Get stock analysis (e.g., /stock TSLA)
/compare SYMBOL1 SYMBOL2 - Compare two stocks (e.g., /compare TSLA NVDA)
/youtube URL QUESTION - Analyze a YouTube video and answer questions
"""

HELP_MESSAGE = """
🤖 Bot Commands:

/stock SYMBOL - Get detailed analysis of a stock
Example: /stock TSLA

/compare SYMBOL1 SYMBOL2 - Compare two stocks
Example: /compare TSLA NVDA

/youtube URL QUESTION - Analyze a YouTube video
Example: /youtube https://youtube.com/watch?v=12345 What are the main points?

The stock analysis includes:
• Current stock price
• Analyst recommendations
• Fundamental analysis
• Key metrics

The YouTube analysis includes:
• Video transcript analysis
• Specific answers to your questions
• Context from the video
"""

# Error Messages
INVALID_STOCK_SYMBOL = "Please provide a stock symbol. Example: /stock TSLA"
INVALID_COMPARE_SYMBOLS = "Please provide two stock symbols. Example: /compare TSLA NVDA"
GENERIC_ERROR = "❌ Error analyzing {}. Please try again later."
COMPARE_ERROR = "Error comparing stocks. Please try again later."
INVALID_COMMAND = "Please use one of the available commands. Type /help to see the list of commands."

# Analysis Prompts
STOCK_ANALYSIS_PROMPT = """Provide a comprehensive analysis of {symbol} including current price, analyst recommendations, and key fundamental metrics. Make it concise but informative. 

Format the response as follows:
1. Current Stock Price and Performance
2. Key Financial Metrics
3. Analyst Recommendations
4. Recent Developments (if any)

Give the data in text format
"""

STOCK_COMPARISON_PROMPT = """Compare {symbol1} and {symbol2} focusing on:
1. Current Stock Prices
2. Key Financial Metrics
3. Performance Comparison
4. Analyst Recommendations
5. Strengths and Weaknesses

Give the data in text format using markdown
"""

# Status Messages
ANALYZING_STATUS = "🔍 Analyzing {}... Please wait."
COMPARING_STATUS = "Comparing {} and {}... Please wait."

# Response Templates
STOCK_RESPONSE_TEMPLATE = "📊 Analysis for {}\n\n{}"
COMPARISON_RESPONSE_TEMPLATE = "📊 Comparison: {} vs {}\n\n{}"

# YouTube Related Messages
YOUTUBE_HELP = """
To analyze a YouTube video and ask questions:
/youtube <video_url> <your_question>

Example: 
/youtube https://youtube.com/watch?v=12345 What are the main points discussed?
"""

INVALID_YOUTUBE_COMMAND = """
Please provide both a YouTube URL and your question.
Example: /youtube https://youtube.com/watch?v=12345 What are the main points?
"""

YOUTUBE_ANALYZING = "🎥 Analyzing video and preparing answer... Please wait."

YOUTUBE_ERROR = "❌ Error analyzing the video. Please check the URL and try again."

YOUTUBE_PROMPT = """
Analyze the following YouTube video {url} transcript and answer this specific question: {question}

Please provide a clear and concise answer based on the video content.
If the question cannot be answered based on the video content, please indicate that.

Format your response in markdown with:
1. Brief context (if relevant)
2. Direct answer to the question
3. Supporting details from the video (if any)
"""

YOUTUBE_RESPONSE_TEMPLATE = """
🎬 *Video Analysis*

*Question:* {question}

{response}

"""
