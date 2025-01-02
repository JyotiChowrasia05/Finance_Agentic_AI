from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')

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

multi_ai_agent = Agent(
 team = [web_search_agent,finance_agent],
 instructions=['Always include sources', 'Use table to display the data'],
 show_tool_calls=True,
 markdown=True
)

multi_ai_agent.print_response('Summarize analyst recomendation and share the lastes new about NVDA',stream=True)

## requirements.txt
phidata
yfinance
packaging
duckduckgo-search
fastapi
uvicorn
groq
python-dotenv
openai

## .env
PHI_API_KEY= 'phi-zL6vpsJJH410KRwlb1Kvh_wK5LK2lBG2NzLm7merFGI'
GROQ_API_KEY= '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'
OPENAI_API_KEY= ''
