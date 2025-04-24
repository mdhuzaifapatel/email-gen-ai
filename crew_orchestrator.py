import json
from crewai import Crew, Process
from agents.reasoning_agent import reasoning_agent
from tasks.email_task import create_email_task

def run_crew(leads, sender):

    # Loads lead's data
    with open(leads, 'r') as f:
        leads_data = json.load(f)
    
    lead = leads_data["leads"][0]
    product = leads_data["product"]

    # Loads sender's data
    with open(sender, 'r') as f:
        senders_data = json.load(f)

    # Creates an Email Task
    task = create_email_task(lead, product, senders_data, reasoning_agent)

    # Creates a Crew
    crew = Crew(
        agents=[reasoning_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    # Runs the Crew
    result = crew.kickoff()

    # Prints the result
    print("Generated Email: ")
    print(result)