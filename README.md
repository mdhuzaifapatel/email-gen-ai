# AI-Powered SDR Email Generator

## Overview
This tool uses CrewAI and OpenAI to generate personalized sales outreach emails based on lead and product data.

## Features
- Single reasoning agent using LLM
- Reads JSON for leads, product, and sender info
- Generates a subject line + personalized email
- Fully containerized with Docker

## Setup

### 1. Add your OpenAI key
Create a `.env` file:

OPENAI_API_KEY=sk-xxxxxx


### 2. Build & Run with Docker
```bash
docker build -t sdr-email-generator .
docker run --rm --env-file .env sdr-email-generator
```