import os
import PyPDF2 as pdf
from flask import Flask, render_template, request,redirect, url_for
from dotenv import load_dotenv
import mysql.connector
from werkzeug.utils import secure_filename
import google.generativeai as genai



app = Flask(__name__)

# Load the environment variables
load_dotenv()

# Connect to MySQL database
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()

# Configure Generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

input_prompt = """
You are a skilled and very experienced ATS (Application Tracking System) with a deep understanding of tech fields, software engineering,
data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive, and you should provide the best assistance for improving resumes. 
Assign the percentage Matching based on Job description and the missing keywords with high accuracy
Resume:{extracted_text}
Description:{jd}
Name: {name}
Mobile No.: {mobile}
Email: {email}

I want the only response in 3 sectors as follows:
• Job Description Match:\n
\n
• Missing Keywords: \n
\n
• Profile Summary: \n
\n
• Suggestions:\n
\n
"""

def process_response(response_text):
    # Split the response into sections
    sections = response_text.split("•")
    
    # Check if sections list has enough elements
    if len(sections) >= 5:
        job_desc_match = sections[1].strip()
        missing_keywords = sections[2].strip()
        profile_summary = sections[3].strip()
        suggestions = sections[4].strip()
        return job_desc_match, missing_keywords, profile_summary, suggestions
    else:
        # Handle case where sections are not as expected
        return "Error: Response format incorrect", "", "", ""
    

@app.route('/', methods=['GET', 'POST'])
def role_selection():
    if request.method == 'POST':
        role = request.form['role']
        if role == 'employee':
            return redirect(url_for('home'))
        elif role == 'employer':
            return redirect(url_for('employer_form'))
    return render_template('role.html')


@app.route('/employee', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        education = request.form['education']
        jd = request.form['jd']
        location = request.form['location']
        mode = request.form['mode']
        type = request.form['type']

        # Process uploaded resume
        if 'resume' in request.files:
            uploaded_file = request.files['resume']
            if uploaded_file.filename != '':
                # Save resume file and get filename
                resume_filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(app.root_path, 'uploads', resume_filename))

                # Insert data into MySQL table
                sql = "INSERT INTO applicant_data (name, mobile, email,education, location, mode, type, resume_text) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
                values = (name, mobile, email,education, location, mode, type, resume_filename)
                cursor.execute(sql, values)
                db.commit()

                # Generate response from Generative AI model
                response = model.generate_content(input_prompt.format(
                    extracted_text="Placeholder for extracted text", jd=jd, name=name, mobile=mobile, email=email))

                # Process the response
                if 'resume' in request.files:
                    uploaded_file = request.files['resume']
                    if uploaded_file.filename != '':
                        reader = pdf.PdfReader(uploaded_file)
                        extracted_text = ""
                        for page in range(len(reader.pages)):
                            page = reader.pages[page]
                            extracted_text += str(page.extract_text())
                        response = model.generate_content(input_prompt.format(
                            extracted_text=extracted_text, jd=jd, name=name, mobile=mobile, email=email))
                        return render_template('result.html', response=response.text)
    return render_template('index.html')

@app.route('/employer', methods=['GET', 'POST'])
def employer_form():
    return render_template("employer.html")

if __name__ == '__main__':
    app.run(debug=True)
