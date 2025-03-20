def get_tables(cursor, db_type):
    queries = {
        "SQLite": "SELECT name FROM sqlite_master WHERE type='table';",
        "PostgreSQL": "SELECT table_name FROM information_schema.tables WHERE table_schema='public';",
        "MySQL": "SHOW TABLES;"
    }
    cursor.execute(queries[db_type])
    return [table[0] for table in cursor.fetchall()]
