import phi
import phi.api
from phi.agent import Agent
from phi.playground import Playground, server_playground_app
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import openai

from dotenv import load_dotenv
load_dotenv()

#openai.api_key=os.getenv('OPENAI_API_KEY')
phi.api = os.getenv('PHI_API_KEY')

## creating web serch agent
web_search_agent = Agent(
 name='Web Search Agent',
 role='Search the web for the information',
 model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
 tools=[DuckDuckGo()],
 instructions=['Always include source'],
 show_tool_calls=True,
 markdown=True
)

## Financial agent

finance_agent = Agent(
 name='Finance AI Agent',
 model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
 tools=[
         YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, 
                       company_news=True)    
       ],
 instructions=['use tables to display data'],
 show_tool_calls=True,
 markdown=True
)

app = Playground(agents=[web_search_agent,finance_agent]).get_app()

if __name__ == "__main__":
 server_playground_app("playground:app", reload = True)
