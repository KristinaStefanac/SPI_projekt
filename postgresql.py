import psycopg2
from sqlalchemy import create_engine

# Postavite veze s bazom podataka
connection = psycopg2.connect(
    host="localhost",
    database="Sales",
    user="postgres",
    password="root"
)

# Stvorite SQLAlchemy engine
engine = create_engine('postgresql+psycopg2://', creator=connection)

# Naziv tablice u bazi podataka
table_name = "dim_customer"

# Spremite DataFrame u PostgreSQL
dim_customer_df.to_sql(table_name, engine, if_exists='replace', index=False)

# Stvaranje tablice
create_table_query = """
CREATE TABLE dim_customer (
    customer_id SERIAL PRIMARY KEY,
    customer_age INTEGER,
    age_group VARCHAR(255),
    customer_gender VARCHAR(255),
    country_id INTEGER,
    country VARCHAR(255),
    state VARCHAR(255),
    dim_customer_id INTEGER,
    date_from DATE,
    date_to DATE
);
"""
cursor = conn.cursor()
cursor.execute(create_table_query)
conn.commit()

# Ubacivanje podataka u tablicu
for _, row in dim_customer_df.iterrows():
    insert_query = """
    INSERT INTO dim_customer (
        customer_age,
        age_group,
        customer_gender,
        country_id,
        country,
        state,
        dim_customer_id,
        date_from,
        date_to
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s
    );
    """
    values = (
        row['customer_age'],
        row['age_group'],
        row['customer_gender'],
        row['country_id'],
        row['Country'],
        row['State'],
        row['dim_customer_id'],
        row['date_from'],
        row['date_to']
    )
    cursor.execute(insert_query, values)
    conn.commit()
# Zatvaranje veze s bazom podataka
cursor.close()
conn.close()
# Zatvorite vezu s bazom podataka
connection.close()