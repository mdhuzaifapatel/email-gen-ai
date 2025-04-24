# Necessary imports
from crewai import Agent

# Reasoning Agent - For analysis & processing of the input data.
reasoning_agent = Agent(
        role="Sales Reasoning Agent",
        goal="Understand the lead and generate a personalized email",
        backstory=(
            "You are an expert sales strategist. You deeply analyze lead profiles "
            "and craft emails that connect product benefits to the lead's background and interests."
        ),
        verbose=True
    )

# Note: More agents for different use cases can be added in this file.