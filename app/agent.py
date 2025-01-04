from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str) -> str:
    symbols = {
        
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

def create_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
        instructions=[
            "Use tables to display data.",
            "If you need to find the symbol for a company, use the get_company_symbol tool.",
        ],
        show_tool_calls=True,
        markdown=True,
        debug_mode=True,
    )

def get_agent_response(query: str) -> str:
    """Get a response from the agent."""
    agent = create_agent()
    try:
        # Use run() instead of respond()
        response = agent.run(message=query, stream=False)
        return response.content if response else "No response received"
    except Exception as e:
        return f"Error getting response: {str(e)}"