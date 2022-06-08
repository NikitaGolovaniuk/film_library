from app.app import db


class UserGroups(db.Model):
    user_group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
