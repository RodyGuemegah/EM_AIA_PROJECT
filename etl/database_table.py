from sqlalchemy import Engine, inspect

inspector = inspect(Engine)
tables = inspector.get_table_names()
print(tables)
