getAllUsersSql = '''
    SELECT * FROM user
'''
registerAUserSql = '''
    INSERT INTO user (name, last_name, password) VALUES (?, ?, ?)
'''
checkPasswordSql = '''
    SELECT * FROM user WHERE id=? AND password=?
'''