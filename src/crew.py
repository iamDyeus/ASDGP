import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	PDFSearchTool,
	WeaviateVectorSearchTool
)




@CrewBase
class PdfSyntheticDataGeneratorCrew:
    """PdfSyntheticDataGenerator crew"""

    
    @agent
    def pdf_data_analyst(self) -> Agent:
        
        embedding_config_pdfsearchtool = dict(
            llm=dict(
                provider="openai",
                config=dict(
                    model="gpt-4o",
                ),
            ),
            embedder=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-3-small",
                ),
            ),
        )
        
        return Agent(
            config=self.agents_config["pdf_data_analyst"],
            tools=[
				PDFSearchTool(config=embedding_config_pdfsearchtool)
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
    def weaviate_data_storage_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["weaviate_data_storage_specialist"],
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
    def synthetic_data_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["synthetic_data_analyst"],
            tools=[
				WeaviateVectorSearchTool(weaviate_api_key="U3JEeUJBaVlHc2hvN3BhNl92WHRnSkRyemwzeGxVOUpsVmowdzE2WVptaFN1dkplVDdDYUZaYlZIZDl3PV92MjAw", weaviate_cluster_url="f8eycaasokq1te2chkjyg.c0.asia-southeast1.gcp.weaviate.cloud")
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
    

    
    @task
    def extract_and_analyze_pdf_data_patterns(self) -> Task:
        return Task(
            config=self.tasks_config["extract_and_analyze_pdf_data_patterns"],
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
    def store_synthetic_data_in_weaviate(self) -> Task:
        return Task(
            config=self.tasks_config["store_synthetic_data_in_weaviate"],
            markdown=False,
        )
    
    @task
    def perform_analytical_queries_on_synthetic_data(self) -> Task:
        return Task(
            config=self.tasks_config["perform_analytical_queries_on_synthetic_data"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the PdfSyntheticDataGenerator crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
