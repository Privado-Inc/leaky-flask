from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    age = db.Column(db.Integer)
    address = db.Column(db.String(120))

    def __repr__(self):
        return '<Task %r>' % self.id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'age': self.age,
            # 'city': self.city,
            # 'state': self.state,
            'address': self.address
        }