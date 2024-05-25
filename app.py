from flask import Flask, render_template, request,render_template, request, flash, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

with open('job_data.json','r') as file :
    JOBS = json.load(file)

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='JobNexus')

# @app.route('/apply/<int:job_id>')
# def apply(job_id):
#     job = next((job for job in JOBS if job['id'] == job_id), None)
#     if job:
#         return render_template('apply.html', job=job)
#     else:
#         return "Job not found", 404




# @app.route('/', methods=['GET', 'POST'])
# def form_data():
#     if request.method == 'POST':
#         full_name = request.form.get('full_name')
#         email_address = request.form.get('email_address')
#         phone_number = request.form.get('phone_number')
#         customFile = request.form.get('customFile')
#         print(full_name, email_address, phone_number, customFile)
    
#     return render_template('apply.html', job={})




# @app.route('/form_data', methods=['POST'])
# def form_data():
#     if request.method == 'POST':
#         full_name = request.form.get('full_name')
#         email_address = request.form.get('email_address')
#         phone_number = request.form.get('phone_number')
#         customFile = request.form.get('customFile')
#         print(f"Full Name: {full_name}, Email: {email_address}, Phone: {phone_number}, Resume: {customFile}")
#         # flash(f"Application submitted for {full_name}!")
#         # return redirect(url_for('home'))
#         return "Form data printed to console"
#     return "Form data not received"



@app.route('/apply/<int:job_id>')
def apply(job_id):
    job = next((job for job in JOBS if job['id'] == job_id), None)
    if job:
        return render_template('apply.html', job=job)
    else:
        return "Job not found", 404

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/form_data', methods=['POST'])
def form_data():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email_address = request.form.get('email_address')
        phone_number = request.form.get('phone_number')
        resume = request.files.get('customFile')

        if resume and resume.filename != '':
            resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume.filename))
            resume_name = resume.filename
        else:
            resume_name = None

        print(f"Full Name: {full_name}, Email: {email_address}, Phone: {phone_number}, Resume: {resume_name}")
        flash('Form data printed to console!', 'success')
        return redirect(url_for('home'))
    return "Form data not received"


if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
