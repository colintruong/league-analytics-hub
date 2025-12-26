from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'teams'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    code = db.Column(db.String(10), nullable = False, unique = True)   # e.g., T1, GEN
    region = db.Column(db.String(10), nullable = False, index = True) # e.g., LCK, LPL
    current_elo = db.Column(db.Integer, default = 1500)
    peak_elo = db.Column(db.Integer, default = 1500)
    global_rank = db.Column(db.Integer)     # e.g., 1, 2, 3
    regional_rank = db.Column(db.Integer)   # e.g., 1, 2, 3 within their region
    
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime,
                           default = lambda: datetime.now(timezone.utc),
                           onupdate = lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Team {self.name} ({self.region})>"