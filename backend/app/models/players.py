from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'
    
    id = db.Column(db.Integer, primary_key = True)
    summoner_name = db.Column(db.String(50), nullable = False)    # e.g., Faker, Caps
    real_name = db.Column(db.String(100), nullable = True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable = True)
    role = db.Column(db.String(10), nullable = False)   # e.g., Top, Jungle, Mid, ADC, Support
    current_rating = db.Column(db.Integer, default = 1500)
    peak_rating = db.Column(db.Integer, default = 1500)
    debut_date = db.Column(db.Date, nullable = True)
    country = db.Column(db.String(50), nullable = True)

    team = db.relationship('Team', backref = 'players', lazy = 'joined')
    
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime,
                           default = lambda: datetime.now(timezone.utc),
                           onupdate = lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Player {self.ingame_name} ({self.country})>"