from db import db
from models.user import User



if __name__ == "__main__":
    db.create_all()
    num = User.query.delete()
    print(f'Deleted {num} rows')
    admin = User(username='admin', email='admin@example.com', password = 'admin123')
    guest = User(username='guest', email='guest@example.com', password = 'guest123')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    print(User.query.all())
    print([[user.username, user.email, user.password]for user in User.query.all()])
