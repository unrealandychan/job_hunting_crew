# Personal Career Coach AI

## Introduction
This project is a personal career coach AI that helps users to find a new job. The AI agent will analysis the candidate's resume, and give recommendations on the job positions that the candidate should apply for. The AI agent will also provide the candidate with the job descriptions of the recommended job positions, and help the candidate to prepare for the job interviews.

## Features
- Analyze the candidate's resume
- Analyze Job Descriptions and extract the keywords
- Compare the candidate's resume with the job descriptions and give recommendations for resume and interview
- Provide future career path recommendations

## How it works
This project uses the following technologies:
- Python
- CrewAI
- OpenAI ChatGPT
- Google Search

For more information regarding CrewAI, please refer to their github repo: https://github.com/joaomdmoura/crewAI

## Installation
To install the required packages, run the following command:
```bash
pip install poetry
poetry install --no-root
```

# Start the AI agent
To start the AI agent, put the resume and the jd in the `input` folder, and run the following command:
```bash
python main.py
```