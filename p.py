from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mysql://root:''@localhost/jntuk', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String()), 
   Column('lastname', String()), 
)

meta.create_all(engine)
ins = students.insert()
ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)