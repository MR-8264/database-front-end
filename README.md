# Flask Form Submission and Data Viewer

## Overview
This Flask-based web application allows users to fill out and submit a form and view the data from all submitted forms. The app connects to a MySQL database using SQLAlchemy and provides sorting, filtering, and column selection features for viewing the stored responses.

## Live Demo
Try the Live App Here: https://database-front-end-production.up.railway.app/

## AI-Assisted Development
This project was developed as part of a client assignment. Since I had little front-end experience at the time, I relied heavily on AI tools like ChatGPT to guide me through the development process. This project highlights how AI can assist developers in tackling new challenges outside their immediate skillset.

## Features
- Form-based user submission
- Stores submissions in a MySQL database
- Displays stored responses with optional sorting and filtering
- Supports column selection and limit-based queries

## Database Setup
This application requires a MySQL database to store submitted form responses.

### 1. Create a MySQL Database
Before running the app, ensure that you have a MySQL database set up. If using a cloud provider (e.g., Railway, GCP, AWS), retrieve the host, username, password, and database name.

### 2. Configure the .env File
Create a `.env` file in the project directory and add your database credentials:
```
MYSQLUSER=your-username
MYSQLPASSWORD=your-password
MYSQLHOST=your-host
MYSQLDATABASE=your-database
MYSQLPORT=3306  # Default MySQL port
```

### 3. Ensure the response Table Exists
If the database is empty, create the required table:
```
CREATE TABLE response (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

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
venv\Scriptsctivate  # Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Application
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
GitHub Profile: https://github.com/MR-8264
