import sqlite3

# Simulated config file or a settings module
CONFIG = {
    "default_table": "users",
    "default_column": "username"
}

def get_data_by_config_value(value):
    # Use a parameterized query to prevent SQL injection
    query = f"SELECT * FROM {CONFIG['default_table']} WHERE {CONFIG['default_column']} = ?"

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(query, (value,))
    result = cursor.fetchall()
    connection.close()

    return result

# Test
print(get_data_by_config_value("admin"))