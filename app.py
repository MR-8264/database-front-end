from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Configure the database
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "3306")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the model
class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("form.html")  # Load the form

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    new_response = Response(name=name, email=email, message=message)

    try:
        db.session.add(new_response)
        db.session.commit()
        return redirect(url_for("view_data"))
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Database error: {e}")  # Logs the error properly
        return "An error occurred while submitting the form. Please try again."
    
@app.route("/view-data", methods=["GET"])
def view_data():
    # Get filter parameters from URL
    limit = request.args.get("limit", type=int)
    sort_by = request.args.get("sort_by", default="id")
    sort_order = request.args.get("order", default="asc")
    selected_columns = request.args.get("columns", default="id,name,email,message,timestamp").split(",")

    # Query responses from the database
    query = Response.query

    # Define valid columns for sorting
    valid_sort_columns = {"id", "name", "email", "message", "timestamp"}

    # Ensure sort_by is a valid column, otherwise default to "id"
    sort_by = sort_by if sort_by in valid_sort_columns else "id"

    # Apply sorting
    query = query.order_by(getattr(Response, sort_by).desc() if sort_order == "desc" else getattr(Response, sort_by).asc())

    # Apply limit if set
    if limit:
        query = query.limit(limit)

    responses = query.all()

    return render_template("view_data.html", responses=responses, selected_columns=selected_columns)

if __name__ == "__main__":
    app.run(debug=True)
