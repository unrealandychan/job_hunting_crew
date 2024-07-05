from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
from langchain_openai import ChatOpenAI

from src.tools.pdf_read_tools import get_pdf_content


@CrewBase
class JobsHuntingCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, options):
        self.llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
        self.search_tool = SerperDevTool()
        self.file_reading_tool = FileReadTool()
        self.options = options

    @agent
    def professional_headhunter(self) -> Agent:
        return Agent(
            config=self.agents_config["professional_headhunter"],
            llm=self.llm,
        )

    @agent
    def personal_career_coach(self) -> Agent:
        return Agent(
            config=self.agents_config["personal_career_coach"],
            llm=self.llm,

        )

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["cover_letter_writer"],
            llm=self.llm
        )

    @task
    def analyze_resume(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_resume_task"],
            agent=self.professional_headhunter(),
            tools=[get_pdf_content]
        )

    @task
    def analyze_job_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_job_requirements_task"],
            agent=self.professional_headhunter(),
            tools=[self.file_reading_tool]
        )

    @task
    def compare_resume_and_job_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["compare_resume_and_job_requirements_task"],
            agent=self.professional_headhunter(),
            tools=[self.search_tool, self.file_reading_tool, get_pdf_content]
        )

    @task
    def future_recommendations(self) -> Task:
        return Task(
            config=self.tasks_config["future_recommendations_task"],
            agent=self.personal_career_coach(),
            tools=[self.search_tool,self.file_reading_tool,get_pdf_content]

        )

    # @task
    # def generate_cover_letter(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["generate_cover_letter_task"],
    #         agent=self.cover_letter_writer()
    #     )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
