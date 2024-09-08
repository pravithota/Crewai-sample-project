from crewai import Agent
import os
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', 
                             verbose=1, 
                             temperature=0.5, 
                             google_api_key=os.getenv('GOOGLE_API_KEY'))

news_researcher = researcher = Agent(
    role='Senior Researcher',
    goal='Reveal ground breaking technologies in {topic}',
    verbose=1,
    llm=llm,
    memory=True,
    backstory=(
        "Driven by curiosity, you are at the forefront of"
        "Innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    allow_delegation=True
)

# creating a write agent with custom tools who is responsible in writing news blog

news_writer = researcher = Agent(
    role='Writer',
    goal='Narrate compelling stories about {topic}',
    verbose=1,
    llm=llm,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    allow_delegation=False
)

