# pipeline connecting frontend to backend

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from fastapi.middleware.cors import CORSMiddleware
from job_scrape import scrape
from typing import Optional, List

import re


app = FastAPI(title="Job Hunter API")

#allow different origins, especially when frontend/backend are sperate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define request model with prompt validation
class PromptRequest(BaseModel):
    prompt: str
    # objective will generate automaticaly but should be dependent on the prompt?

    # validation logic for incoming prompt strings
    @field_validator('prompt')
    @classmethod
    def validate_string(cls, v: str):
        #prompt length constraints
        if not (10 <= len(v) <= 800):
            raise ValueError('Prompt must be between 10 and 800 characters.')
        
        
        # reject any unsafe HTML script tags
        if '<script>' in v.lower() or '</script>' in v.lower():
            raise ValueError('Input contains unsafe HTML tags.')
    
        # reject dangerous characher sequences
        dangerous_chars = ['--', ';', '/*', '\'', '*/', '\"', '==']
        if any(pattern in v for pattern in dangerous_chars):
            raise ValueError('Input contains potential dangerous special pattern or character')
       
        # use regex to detect more malicious inputs
        regex_patterns = [
            #prevent xss
            re.compile(r"<script.*?>", re.IGNORECASE),
            re.compile(r"eval\(", re.IGNORECASE),
            # reject hex values like 0xDEADBEEF
            re.compile(r"0x[0-9a-f]+", re.IGNORECASE),
        ]
        for pattern in regex_patterns:
            if pattern.search(v):
                raise ValueError("Input contains a forbidden pattern.")
        
        return v

class Job(BaseModel):
    title: str
    company: str
    location: str
    salary: Optional[str]
    link: str


    
class Result(BaseModel):
    # job, company, location, salary, url
    final_list = List[Job]


@app.get("/prompt")
async def handle_prompt(prompt: str):
    global last_error_message

    # manually validating prompt
    try:
        PromptRequest(prompt=prompt)
    except ValueError as ve:
        last_error_message = str(ve)
        raise HTTPException(status_code=400, detail=last_error_message)
    except Exception:
        last_error_message = "Invalid job request."
        raise HTTPException(status_code=422, detail=last_error_message)
    """
    Given a prompt, start the scraping process.
    """
    try:
        jobs = scrape(prompt)
        return Result(final_list=jobs)
    except Exception as ex:
        last_error_message = str(ex)
        raise HTTPException(status_code=500, detail="Failed to scrape jobs")