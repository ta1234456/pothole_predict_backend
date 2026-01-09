import os

class Config:
    """Application configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000
    
    # Model configuration
    MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models')
    
    # Upload configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
