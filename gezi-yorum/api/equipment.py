from sqlalchemy import create_engine


engine = create_engine("oracle://hr:1@ORCL", echo=True, future=True)
