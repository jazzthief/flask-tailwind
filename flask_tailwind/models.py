from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TestModel(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255))

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'<User {self.data}>'
