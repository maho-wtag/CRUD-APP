from sqlalchemy import craete_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306")

meta = MetaData()
connection = engine.connect()
