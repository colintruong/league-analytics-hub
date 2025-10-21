import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig:
    """Database configuration settings"""
    
    # For development, we'll use SQLite (simple file-based database)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///league_analytics.db'
    
    # Turn off modification tracking (saves memory)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Show SQL queries in console (helpful for learning)
    SQLALCHEMY_ECHO = True