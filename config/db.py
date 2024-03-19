from sqlalchemy import create_engine, MetaData

engine = create_engine(f"mysql+mysqlconnector://root:12345678@localhost:3306/Student")

meta = MetaData()
connection = engine.connect()
