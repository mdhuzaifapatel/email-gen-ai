# Necessary imports
from crew_orchestrator import run_crew
from dotenv import load_dotenv

# Loads .env for OPENAI_API_KEY
load_dotenv()

# Main function
if __name__ == "__main__":

    # File paths for input data
    leads_file_path = "data/leads_info.json"
    senders_file_path = "data/senders_info.json"

    # Execute the crew
    run_crew(leads=leads_file_path, sender=senders_file_path)
