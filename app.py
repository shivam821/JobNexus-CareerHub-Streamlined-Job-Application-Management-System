from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer (Backend Development)',
        'location': 'Bangalore, Karnataka, India',
        'salary': 'INR 12-18 lakhs per annum',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Pune, Maharashtra, India',
        'salary': 'INR 15-22 lakhs per annum',
    },
    {
        'id': 3,
        'title': 'Frontend Developer (React.js)',
        'location': 'Hyderabad, Telangana, India',
        'salary': 'INR 10-15 lakhs per annum',
    },
    {
        'id': 4,
        'title': 'DevOps Engineer',
        'location': 'Gurgaon, Haryana, India',
        'salary': 'INR 14-20 lakhs per annum',
    },
]


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
