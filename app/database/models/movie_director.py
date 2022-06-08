from app.app import db


class MovieDirector(db.Model):
    movie_id = db.relationship('Movie')

    