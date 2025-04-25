# AI-Powered SDR Email Generator – Solution Summary

## Objective

The goal of this prototype is to simulate an AI-driven workflow that automates personalized email generation for SDRs using lead data and product context. The system is designed using an agentic framework (CrewAI), integrates OpenAI's LLM, and is containerized using Docker for easy deployment.

---

## Approach

### 1. Data Simulation
- Created `leads_data.json` to simulate scraped LinkedIn data (name, title, company, interests).
- Added `senders_info.json` to include sender name, role, and company for realistic email sign-offs (not part of original prompt but necessary for email quality).

### 2. LLM Integration
- Used OpenAI’s API for using the LLM.
- Constructed a structured prompt combining lead info, product details, and sender identity to guide the model in producing relevant email subject lines and bodies.

### 3. Agentic Framework
- Used CrewAI to implement a “Reasoning Agent” as specified in the prompt.
- This agent is responsible for interpreting the input context and generating email content based on it.

### 4. Modular Code Design
- The application is broken into logical components:
  - Data loading and validation
  - CrewAI agent and task configuration
  - LLM invocation and response parsing
  - Execution logic (`main.py`)

### 5. Docker Containerization
- Wrote a `Dockerfile`
- Loads environment variables from `.env` for API key injection.
- Commands for execution:
  - Building a docker image
    ```bash
    docker build -t sdr-email-generator .
    ```
  - Run the docker image as container
    ```bash
    docker run --rm --env-file .env sdr-email-generator
    ```
    
- Single-command (for both building & running): 
  ```bash
  docker build -t sdr-email-generator . && docker run --rm --env-file .env sdr-email-generator
  ```

## Assumptions Made
- Only one lead is processed per run (can be expanded easily).
- The sender’s identity (name, role, company) is assumed and added via sender_info.json.
- Output is terminal-based — no file exports or UI for this prototype.
- OpenAI API key is user-provided and secured via .env.

## Tools & References
- Used ChatGPT for guidance on:
  - CrewAI setup and best practices
  - Structuring the README and documentation
