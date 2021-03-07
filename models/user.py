from db import db

class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username = username).first()


    @classmethod
    def get_by_usernames(cls, usernames):
        query = cls.query.filter_by(cls.username.in_(usernames)).all()


    @classmethod
    def get_by_id(cls, id_):
        return cls.query.filter_by(id = id_).first()


    @classmethod
    def get_by_ids(cls, ids):
        query = cls.query.filter_by(cls.id.in_(ids)).all()


    def json(self):
        return {'username':self.username,'password':self.password,'email':self.email}
