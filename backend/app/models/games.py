from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key = True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable = False, index = True)
    game_number = db.Column(db.Integer, nullable = False)  # e.g., Game 1, Game 2
    winner_side = db.Column(db.String(10), nullable = False)  # e.g., blue, red
    duration_minutes = db.Column(db.Integer, nullable = False)
    start_time = db.Column(db.DateTime, nullable = False)
    end_time = db.Column(db.DateTime, nullable = True)

    match = db.relationship('Match', backref = db.backref('games', lazy = 'select'))

    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, 
                           default = lambda: datetime.now(timezone.utc), 
                           onupdate = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Game {self.match_id} - Game {self.game_number}>"