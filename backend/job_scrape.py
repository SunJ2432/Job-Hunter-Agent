# take in prompt, first filter job postings using OSS
# then extract real job websites
# within each, scrape each job posting

from bs4 import BeautifulSoup
from typing import Dict, List


import requests

# parsing prompt using gpt 
def parse_gpt_oss(prompt: str) -> list:
    #TODO: add real API logic
    return []


# build logic for entire scraping process
def scrape(prompt: str) -> list:
    gpt_oss = (
        f"Given the job search prompt: '{prompt}', give me 5-10 urls to job board websites that have relevant postings, consider Indeed, LinkedIn, etc."
    )
    try:
        postings = parse_gpt_oss(gpt_oss)
    except Exception:
        print("GPT-OSS failed")
        return []
    
    jobs = []
    for board in postings:
        if board.startswith("http"):
            try:
                job = scrape_job_from_posting(board)
                jobs.extend(job)
            except Exception as e:
                print(f"Failed to scrape {board}: {e}")
    return jobs

# for each individual job board, scrape the webpage
def scrape_job_from_posting(str) -> List[Dict]:
    # using beautifulSoup to scrape webpages
    # but how to do it dynamically? with different headers in HTML
    #TODO: implement scraping logic
    return []
