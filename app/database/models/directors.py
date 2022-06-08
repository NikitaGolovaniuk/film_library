from app.app import db


class Directors(db.Models):
    director_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
