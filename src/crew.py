import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
load_dotenv()




@CrewBase
class PdfSyntheticDataGeneratorCrew:
    """PdfSyntheticDataGenerator crew"""

    
    @agent
    def csv_data_pattern_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["csv_data_pattern_analyst"],
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def synthetic_data_generator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["synthetic_data_generator"],
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def data_quality_orchestrator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["data_quality_orchestrator"],
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def multi_format_data_storage_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["multi_format_data_storage_specialist"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def analyze_csv_data_template_for_patterns(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_csv_data_template_for_patterns"],
            markdown=False,
        )
    
    @task
    def generate_synthetic_data_rows(self) -> Task:
        return Task(
            config=self.tasks_config["generate_synthetic_data_rows"],
            markdown=False,
        )
    
    @task
    def validate_and_finalize_synthetic_dataset(self) -> Task:
        return Task(
            config=self.tasks_config["validate_and_finalize_synthetic_dataset"],
            markdown=False,
        )
    
    @task
    def store_synthetic_data_in_multiple_formats(self) -> Task:
        return Task(
            config=self.tasks_config["store_synthetic_data_in_multiple_formats"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the PdfSyntheticDataGenerator crew and saves output to a file"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
        )