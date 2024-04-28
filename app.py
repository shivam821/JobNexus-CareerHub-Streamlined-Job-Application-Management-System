from flask import Flask, render_template
import json

app = Flask(__name__)

with open('job_data.json','r') as file :
    JOBS = json.load(file)

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='JobNexus')


@app.route('/apply/<int:job_id>')
def apply(job_id):
    job = next((job for job in JOBS if job['id'] == job_id), None)
    if job:
        return render_template('apply.html', job=job)
    else:
        return "Job not found", 404


if __name__ == '__main__':
    app.run(debug=True)
