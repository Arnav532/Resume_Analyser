import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///resumes.db'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'pdf'}
    OPENAI_API_KEY = 'yourapikey'  # In production, use environment variables