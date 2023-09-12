from flask import Flask, render_template, request, jsonify

from resume.resume_generator import generate_custom_resume

import tiktoken

app = Flask(__name__)

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_resume", methods=["POST"])
def generate_resume():
    resume_text = request.form.get("resume")
    job_description = request.form.get("job_description")

    # Check the length of both texts
    total_length = len(encoding.encode(job_description)) + len(encoding.encode(resume_text))

    if total_length > 3500:
        return jsonify({"error": "Combined length of resume and job description is too long."})

    # Call your function to generate custom resume
    generated_resume = generate_custom_resume(job_description, resume_text)

    return jsonify(generated_resume)

if __name__ == "__main__":
    app.run(debug=True)