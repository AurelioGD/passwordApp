createTableUserSql = '''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXTO NOT NULL,
        last_name TEXTO NOT NULL,
        password TEXT NOT NULL
    )
'''
createTablePasswordSql = '''
    CREATE TABLE IF NOT EXISTS password (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT NOT NULL,
        user_name TEXT NOT NULL,
        password TEXTO NOT NULL,
        description TEXT 
    )
'''