from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key = True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'), nullable = False, index = True)
    team1_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable = False, index = True)
    team2_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable = False, index = True)
    winner_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable = True)
    scheduled_time = db.Column(db.DateTime, nullable = False)
    start_time = db.Column(db.DateTime, nullable = True)
    end_time = db.Column(db.DateTime, nullable = True)
    best_of = db.Column(db.Integer, nullable = False)   # e.g., 1, 3, 5
    status = db.Column(db.String(20), nullable = False, default = 'scheduled')  # e.g., scheduled, ongoing, completed
    patch_version = db.Column(db.String(20), nullable = True)   # e.g., 25.6

    tournament = db.relationship('Tournament', backref = db.backref('matches', lazy = 'select'))
    team1 = db.relationship('Team', foreign_keys = [team1_id])
    team2 = db.relationship('Team', foreign_keys = [team2_id])
    winner = db.relationship('Team', foreign_keys = [winner_id])

    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, 
                           default = lambda: datetime.now(timezone.utc),
                           onupdate = lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Match {self.id} - Team {self.team1_id} vs Team {self.team2_id} ({self.status})>"