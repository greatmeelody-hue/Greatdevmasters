from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///greatdevmaster.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(160), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

with app.app_context():
    db.create_all()

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/contact")
def contact():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    subject = (data.get("subject") or "").strip()
    message = (data.get("message") or "").strip()

    if not all([name, email, subject, message]):
        return jsonify(ok=False, message="Please complete every field."), 400
    if len(name) > 100 or len(email) > 150 or len(subject) > 160 or len(message) > 5000:
        return jsonify(ok=False, message="One or more fields are too long."), 400
    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        return jsonify(ok=False, message="Please enter a valid email address."), 400

    db.session.add(ContactMessage(name=name, email=email, subject=subject, message=message))
    db.session.commit()
    return jsonify(ok=True, message="Thanks! Your message has been saved.")

if __name__ == "__main__":
    app.run(debug=True)
