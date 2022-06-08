from app.app import db


class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    release_date = db.Column(db.DateTime(timezone=True), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(500), nullable=True)
    user_id = db.relationship
