from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'experience': self.experience,
            'education': self.education,
            'skills': self.skills,
            'social_links': self.social_links,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }