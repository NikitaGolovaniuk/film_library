from app.app import db


class Genres(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
