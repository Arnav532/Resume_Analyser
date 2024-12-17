import os
from jinja2 import TemplateNotFound
from openai import OpenAI
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import PyPDF2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)


class ResumeData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    experience = db.Column(db.Text)
    education = db.Column(db.Text)
    skills = db.Column(db.Text)
    social_links = db.Column(db.Text)
    extracted_text = db.Column(db.Text)

def extract_text_from_pdf(file_path): #defineing a function to extract text from pdf
    with open(file_path, 'rb') as file: #open the pdf in binary read mode 
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''   # Initialize an empty string to store the text
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text





api_key = 'your-api-key'
if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
client = OpenAI(api_key=api_key)

def parse_resume_with_openai(text): # Defineing a function to parse a resume using OpenAI
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Extract the following information from the given resume text :\n\nName:\nPhone Number:\nEmail:\nExperience:\nEducation:\nSkills:\nSocial Links:\n\nResume Text:\n{text}"
            }
            ],
    model="gpt-3.5-turbo",
    max_tokens=3000,
        temperature=0.5,

)

    
    parsed_data = response.choices[0].message.content.strip().split('\n')
    resume_data = {}
    for line in parsed_data:
        if ':' in line:
            field, value = line.split(':', 1)
            resume_data[field.strip()] = value.strip()
    
    return resume_data

def save_parsed_data_to_db(parsed_data , text): # Defineing a function to save the parsed resume data to the database
    resume_data = ResumeData(
        name=parsed_data.get('Name', ''),
        phone=parsed_data.get('Phone Number', ''),
        email=parsed_data.get('Email', ''),
        experience=parsed_data.get('Experience', ''),
        education=parsed_data.get('Education', ''),
        skills=parsed_data.get('Skills', ''),
        social_links=parsed_data.get('Social Links', ''),
        extracted_text=text 
    )
    db.session.add(resume_data)
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']  # Get the uploaded resume file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)   # Save the file to the upload folder
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        parsed_data = parse_resume_with_openai(text)
        save_parsed_data_to_db(parsed_data, text)
        try:
            return render_template('results.html', data=parsed_data)
        except TemplateNotFound:
            return 'Template not found: result.html'
    return render_template('index.html')
        

@app.route('/resumes')
def resumes():
    resumes = ResumeData.query.all()
    return render_template('resumes.html', resumes=resumes)


@app.route('/resumes/<int:resume_id>')
def view_resume(resume_id):
    resume = ResumeData.query.get(resume_id)
    return render_template('view_resume.html', resume=resume)

@app.route('/extracts/<int:resume_id>')
def extracts(resume_id):
    resume = ResumeData.query.get(resume_id)
    return render_template('extracts.html', resume=resume)

if __name__ == '__main__':
     with app.app_context():
        db.create_all() # creating database variables 
        app.run(debug=True)