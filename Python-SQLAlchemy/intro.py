import sqlalchemy as sa
import pandas as pd

# Crea el engine
engine = sa.create_engine("sqlite:///Chinook.sqlite")
print(engine.table_names())

# Con SQLAlchemy
with engine.connect() as con:
    # Query
    rs = con.execute("SELECT * FROM Artist")

    # Conversion a DataFrame
    df = pd.DataFrame(rs.fetchall())
    # df = pd.DataFrame(rs.fetchmany(size=5))

    # Nombre de columnas del DataFrame
    df.columns = rs.keys()

# Con Pandas
df = pd.read_sql_query("SELECT * FROM Album", engine)


print(df.head())
