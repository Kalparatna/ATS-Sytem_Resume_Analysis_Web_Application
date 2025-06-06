# Resume Analysis Web Application

## Overview

This web application is designed for employees to upload their resumes and receive AI-powered feedback based on job descriptions. Employers can post job descriptions and evaluate candidate resumes. The AI matches resumes to job descriptions, highlights missing keywords, and provides suggestions for improving the resume.

## Features

- **Employee Dashboard:**
  - Upload resume.
  - Receive AI-generated feedback on resume match with job description.
  - Suggestions for improving resume.

- **Employer Dashboard:**
  - Post job descriptions.
  - Review and shortlist candidates based on resume match.
  - View top candidates based on resume analysis score.

## Technologies Used

- **Backend:** Flask (Python)
- **Database:** MySQL
- **AI Integration:** Google Gemini (Generative AI)
- **File Handling:** PyPDF2 (for extracting resume text from PDFs)
- **Environment Variables:** Dotenv for managing sensitive data
- **Frontend:** HTML, CSS, and basic templates with Flask

## Installation

1. Clone the repository.
   ```bash
   git clone (https://github.com/Kalparatna/ATS-Sytem_Resume_Analysis_Web_Application.git)
   cd <project-folder>
Install required packages:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file and include the following:
makefile
Copy code
DB_HOST=<your-database-host>
DB_USER=<your-database-username>
DB_PASSWORD=<your-database-password>
DB_NAME=<your-database-name>
GOOGLE_API_KEY=<your-google-api-key>
Run the application:

```bash

python app.py
```
Usage
Employee: Select "employee" and upload your resume to receive feedback.
Employer: Select "employer" to post a job description and view the top candidates based on their resume matches.

