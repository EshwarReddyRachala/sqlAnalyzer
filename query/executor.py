def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results, columns = cursor.fetchall(), [desc[0] for desc in cursor.description]
    cursor.close()
    return results, columns
