from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tournament(db.Model):
    __tablename__ = 'tournaments'

    tournament_teams = db.Table('tournament_teams',
        db.Column('tournament_id', db.Integer, db.ForeignKey('tournaments.id')),
        db.Column('team_id', db.Integer, db.ForeignKey('teams.id'))
    )

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)  # e.g., LCK Spring 2025, World Championship 2025
    slug = db.Column(db.String(100), nullable = False, unique = True)
    region = db.Column(db.String(50), nullable = False, index = True)
    tier = db.Column(db.String(20), nullable = False)  # e.g., Regional, International
    start_date = db.Column(db.Date, nullable = False)
    end_date = db.Column(db.Date, nullable = True)
    prize_pool = db.Column(db.Integer, nullable = True)  # in USD
    status = db.Column(db.String(20), nullable = False, default = 'scheduled', index = True)  # e.g., scheduled, ongoing, completed

    teams = db.relationship('Team', secondary = tournament_teams, backref = 'tournaments', lazy = 'select')

    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, 
                           default = lambda: datetime.now(timezone.utc),
                           onupdate = lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Tournament {self.name})>"