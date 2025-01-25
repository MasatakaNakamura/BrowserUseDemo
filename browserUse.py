from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

async def main():
    load_dotenv(verbose=True)

    userid = os.environ.get("USERID")
    password = os.environ.get("PASSWORD")

    agent = Agent(
        task=f"https://system.ginga.info/ohana/に、ユーザID = {userid}, パスワード ={password}でログインしてください",
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())