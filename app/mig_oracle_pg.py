import cx_Oracle
import psycopg2
from psycopg2 import sql

# Oracle and PostgreSQL connection configurations
ORACLE_CONFIG = {
    'user': 'oracle_user',
    'password': 'oracle_password',
    'dsn': 'oracle_dsn'
}

POSTGRES_CONFIG = {
    'dbname': 'postgres_db',
    'user': 'postgres_user',
    'password': 'postgres_password',
    'host': 'localhost',
    'port': 5432
}

def migrate_oracle_to_postgres():
    # Connect to Oracle
    oracle_conn = cx_Oracle.connect(**ORACLE_CONFIG)
    oracle_cursor = oracle_conn.cursor()

    # Connect to PostgreSQL
    postgres_conn = psycopg2.connect(**POSTGRES_CONFIG)
    postgres_cursor = postgres_conn.cursor()

    try:
        # Fetch all table names from Oracle schema
        oracle_cursor.execute("""
            SELECT table_name 
            FROM user_tables
        """)
        tables = oracle_cursor.fetchall()

        for table_name_tuple in tables:
            table_name = table_name_tuple[0]
            print(f"Migrating table: {table_name}")

            # Fetch table structure from Oracle
            oracle_cursor.execute(f"""
                SELECT column_name, data_type, data_length 
                FROM user_tab_columns 
                WHERE table_name = '{table_name}'
            """)
            columns = oracle_cursor.fetchall()

            # Create table in PostgreSQL
            create_table_query = f"CREATE TABLE {table_name} ("
            column_definitions = []
            for column_name, data_type, data_length in columns:
                pg_data_type = map_oracle_to_postgres_type(data_type, data_length)
                column_definitions.append(f"{column_name} {pg_data_type}")
            create_table_query += ", ".join(column_definitions) + ");"
            postgres_cursor.execute(create_table_query)
            postgres_conn.commit()

            # Fetch all data from Oracle table
            oracle_cursor.execute(f"SELECT * FROM {table_name}")
            rows = oracle_cursor.fetchall()

            # Insert data into PostgreSQL table
            if rows:
                placeholders = ", ".join(["%s"] * len(rows[0]))
                insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                postgres_cursor.executemany(insert_query, rows)
                postgres_conn.commit()

    except Exception as e:
        print(f"Error: {e}")
        postgres_conn.rollback()
    finally:
        # Close connections
        oracle_cursor.close()
        oracle_conn.close()
        postgres_cursor.close()
        postgres_conn.close()

def map_oracle_to_postgres_type(oracle_type, length):
    """Map Oracle data types to PostgreSQL data types."""
    oracle_to_postgres = {
        'VARCHAR2': 'VARCHAR',
        'NUMBER': 'NUMERIC',
        'DATE': 'TIMESTAMP',
        'CHAR': 'CHAR',
        'CLOB': 'TEXT',
        'BLOB': 'BYTEA'
    }
    pg_type = oracle_to_postgres.get(oracle_type, 'TEXT')
    if pg_type == 'VARCHAR' and length:
        return f"VARCHAR({length})"
    return pg_type

if __name__ == "__main__":
    migrate_oracle_to_postgres()