createNewPasswordSql = '''
    INSERT INTO password (name, url, user_name, password, description)
    VALUES (?, ?, ?, ?, ?)
'''
getAllPasswordsSql = '''
    SELECT * FROM password
'''
getPasswordByIdSql = '''
    SELECT * FROM password WHERE id=?
'''
modifyAPasswordSql = '''
    UPDATE password SET name = ?, url = ?, user_name = ?, password = ?, description = ? WHERE id = ? 
'''
deletePasswordByIdSql = '''
    DELETE FROM password WHERE id = ?
'''