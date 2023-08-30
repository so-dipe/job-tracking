from resume_generator import generate_custom_resume

def main():
    with open("resume/example_resume.txt", "r") as resume_file:
        resume = resume_file.read()

    with open("resume/example_job_description.txt", "r") as job_description_file:
        job_description = job_description_file.read()

    generated_resume = generate_custom_resume(resume, job_description)
    print("Generated Resume:")
    print(generated_resume)

if __name__ == "__main__":
    main()