from crewai import Crew, Process
from agents import news_researcher,news_writer
from tasks import research_task, write_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents = [news_researcher, news_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,

)

# Starting the task execution process with enhanced feedback

result = crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)