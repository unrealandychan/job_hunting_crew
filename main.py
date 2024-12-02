import argparse
import os

from dotenv import load_dotenv
from datetime import datetime
from src.crew import JobsHuntingCrew

# Load the .env file here
load_dotenv()


# Define the main function to parse the arguments
def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()

    arguments = [
        ("--resume_path", {"type": str, "default": "input/resume_eddie.pdf",
                           "help": "input file path to the Resume"}),
        ("--job_description_path", {"type": str, "default": "input/jd.txt",
                                  "help": "input file path to the Job Description"}),
        ("--openai_key", {"type": str,
                          "default": "", "help": "OpenAI API key"}),
        ("--google_key", {"type": str, "default": "",
                          "help": "Google Cloud API key"}),
        ("--llm_provider", {"type": str, "default": "openai"}),
        ("--model", {"type": str, "default": "gpt-4o",
                     "help": "Model to use for translation, e.g., 'gpt-3.5-turbo' or 'gpt-4'"}),
    ]

    for argument, kwargs in arguments:
        parser.add_argument(argument, **kwargs)

    options = parser.parse_args()
    APIKEY = options.openai_key or os.environ.get("OPENAI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not APIKEY:
        raise Exception("Please provide your LLM API key")
    return options


# This is the main class to start your own crew
if __name__ == "__main__":
    # Arguments Parser

    print("## Job Hunting Crew Start here ##")
    print("-------------------------------")
    options = parse_arguments()
    inputs = {
        "resume_path": options.resume_path,
        "job_description_path": options.job_description_path,
    }

    crew = JobsHuntingCrew(options).crew()
    final_result = crew.kickoff(inputs=inputs)
    print("\n\n########################")
    print("## Saving your result into /output folder ##")
    print("########################\n")
    # Save the final result here
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    os.mkdir(f"output/{date}")
    with open(f"output/{date}/final_output.txt", "w+") as text_file:
        text_file.write(final_result)

    # And Save result for each task
    for index, task in enumerate(crew.tasks):
        with open(f"output/{date}/task_{index+1}_output.txt", "w+") as text_file:
            text_file.write(task.output.description)
            text_file.write(task.output.raw_output)


