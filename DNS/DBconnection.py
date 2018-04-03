from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql://ubuntu:528@10.0.0.9/cdn')
engine = create_engine('postgresql://ubuntu:528@128.31.25.73/cdn')

Session = sessionmaker(bind=engine)
session = Session()
for instance in session.query('users'):
    print(instance)
# print(session.query('users'))
