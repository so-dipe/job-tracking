import os
import json
from dotenv import load_dotenv

import openai

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

with open("resume/system_prompt.txt", 'r') as f:
    system_prompt = f.read()


def generate_custom_resume(resume, job_description, system_prompt=system_prompt):
    system_prompt = f"{system_prompt}"
    user_prompt = (
        f"""Please generate a tailored resume for a candidate applying for the role given below.\n"""
        f"""Job Description: {job_description}\n"""
        f"""Use the following resume as a guide:\n {resume}"""
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    generated_resume = response.choices[0].message["content"].strip()
    return generated_resume

def discuss(generated_resume):
    pass

def resume_to_json(generated_resume):
    pass