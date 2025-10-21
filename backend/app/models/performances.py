from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Performance(db.Model):
    __tablename__ = 'performances'

    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable = False, index = True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable = False, index = True)
    side = db.Column(db.String(10), nullable = False)  # e.g., blue, red
    champion = db.Column(db.String(50), nullable = False)
    kills = db.Column(db.Integer, nullable = False, default = 0)
    deaths = db.Column(db.Integer, nullable = False, default = 0)
    assists = db.Column(db.Integer, nullable = False, default = 0)
    damage_to_champions = db.Column(db.Integer, nullable = False, default = 0)
    damage_per_minute = db.Column(db.Float, nullable = False, default = 0.0)
    gold_earned = db.Column(db.Integer, nullable = False, default = 0)
    cs_total = db.Column(db.Integer, nullable = False, default = 0)
    cs_per_minute = db.Column(db.Float, nullable = False, default = 0.0)
    vision_score = db.Column(db.Integer, nullable = False, default = 0)
    performance_rating = db.Column(db.Float, nullable = False, default = 0.0)

    player = db.relationship('Player', backref = db.backref('performances', lazy = 'select'))
    game = db.relationship('Game', backref = db.backref('performances', lazy = 'select'))

    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, 
                           default = lambda: datetime.now(timezone.utc), 
                           onupdate = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Performance of {self.player_id} in Game {self.game_id}: {self.performance_rating}>"