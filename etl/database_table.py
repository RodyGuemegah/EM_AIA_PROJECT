from sqlalchemy import inspect

inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)
