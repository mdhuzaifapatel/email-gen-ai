# Necessary imports
from crewai import Task

# Email Task for the Agent
def create_email_task(lead, product, sender, reasoning_agent):
    return Task(
        description=
            f"Using the following lead profile: {lead['name']}, a {lead['job_title']} at "
            f"{lead['company']} interested in {', '.join(lead['interests'])}, and the product "
            f"'{product['name']}': {product['description']}, generate a personalized email. "
            "Include a subject line and a professional email body that resonates with the lead’s role and interests."
            "End the email with a professional sign-off using the sender's details: "
            f"Name: {sender['name']}, Position: {sender['designation']}, Company: {sender['company']}, Contact information: {sender['email']}.",

        expected_output="A compelling email subject with a personalized email body tailored to the lead..",
        agent=reasoning_agent,
    )


# Note: More tasks can be added in this file as required.