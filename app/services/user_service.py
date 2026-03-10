from app.extensions import db
from app.models.user import User


def get_all_users():
    return User.query.all()


def get_user(user_id):
    return User.query.get(user_id)


def create_user(name, email):

    user = User(name=name, email=email)

    db.session.add(user)

    db.session.commit()

    return user


def update_user(user, name, email):

    user.name = name

    user.email = email

    db.session.commit()


def delete_user(user):

    db.session.delete(user)

    db.session.commit()