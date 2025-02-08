import sqlite3 
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database # имя базы данных
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute(""""CREATE TABLE projects('project_id INTEGER PRIMARY KEY, user_id INTEGER PRIMARY KEY, project_name TEXT NOT NULL, description TEXT, url TEXT, status_id INTEGER,  REFERENCES status(status_id)""")
            conn.execute(""""CREATE TABLE status id('status_id INTEGER, PRIMARY KEY, status name TEXT PRIMARY KEY)""")
            conn.execute(""""CREATE TABLE skill project(skill_id INTENGER PRIMARY KEY, REFERENCES skill name (skill name))""")
            conn.execute(""""CREATE TABLE skill name(REFERENCES skill project(skill_id), skill name TEXT, PRIMARY KEY, REFERENCES projects(user_id) )""")
            conn.commit()
   
        if __name__ == '__main__':
            manager = DB_Manager(DATABASE)
            manager.create_tables()


