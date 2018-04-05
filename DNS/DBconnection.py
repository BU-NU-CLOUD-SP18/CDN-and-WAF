from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Users

engine = create_engine('postgresql://ubuntu:528@10.0.0.9/cdn')
# engine = create_engine('postgresql://ubuntu:528@128.31.25.73/cdn')

Session = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine))
for instance in session.query(Users.email).all():
    print(instance)
# print(session.query('users'))
