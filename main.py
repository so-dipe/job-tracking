from flask import Flask, render_template, request, jsonify

from resume.resume_generator import generate_custom_resume

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_resume", methods=["POST"])
def generate_resume():
    resume_text = request.form.get("resume")
    job_description = request.form.get("job_description")

    # Call your function to generate custom resume
    generated_resume = generate_custom_resume(resume_text, job_description)
    
    return jsonify({"generated_resume": generated_resume})

if __name__ == "__main__":
    app.run(debug=True)