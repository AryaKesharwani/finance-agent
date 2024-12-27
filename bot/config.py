# Bot Messages
WELCOME_MESSAGE = """
Welcome to the Stock & Crypto Analysis Bot! 🚀

Available commands:
/start - Show this welcome message
/help - Show help message
/stock SYMBOL - Get stock analysis (e.g., /stock TSLA)
/compare SYMBOL1 SYMBOL2 - Compare two stocks (e.g., /compare TSLA NVDA)
"""

HELP_MESSAGE = """
🤖 Stock & Crypto Bot Commands:

/stock SYMBOL - Get detailed analysis of a stock
Example: /stock TSLA

/compare SYMBOL1 SYMBOL2 - Compare two stocks
Example: /compare TSLA NVDA

The analysis includes:
• Current stock price
• Analyst recommendations
• Fundamental analysis
• Key metrics
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
