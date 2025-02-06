# Flask Form Submission and Data Viewer

## Overview
This Flask-based web application allows users to submit responses through a form and view submitted data in a structured format. The app connects to a MySQL database using SQLAlchemy and provides sorting, filtering, and column selection features for viewing the stored responses.

## AI-Assisted Development
This project was developed as part of a client assignment. Since I had little front-end experience at the time, I relied heavily on AI tools like ChatGPT to guide me through the development process. This project highlights how AI can assist developers in tackling new challenges outside their immediate skillset.

## Features
- Form-based user submission (name, email, message)
- Stores submissions in a MySQL database
- Displays stored responses with optional sorting and filtering
- Supports column selection and limit-based queries

## Installation

### 1. Clone the Repository
```
git clone https://github.com/YOUR-USERNAME/your-repo.git
cd your-repo
```

### 2. Set Up a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Configure Database Connection
1. Create a `.env` file in the project directory with your database credentials:
```
SQLALCHEMY_DATABASE_URI=mysql://your-username:your-password@your-host/your-database
SQLALCHEMY_TRACK_MODIFICATIONS=False
```
2. Ensure MySQL is running and the database is created.

### 5. Run the Application
```
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## Routes
- `/` - Displays the form for user submission.
- `/submit` - Handles form submission and stores data in the database.
- `/view-data` - Displays submitted data with sorting, filtering, and column selection.

## Author
Mike Bibeau  
[GitHub Profile](https://github.com/MR-8264)
