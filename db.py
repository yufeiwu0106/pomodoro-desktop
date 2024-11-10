import sqlite3

class Database:
    DB_NAME = "pomodoro.db"

    def init(self):
        conn = sqlite3.connect(self.DB_NAME)
        print("Opened database successfully")

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users
            (name varchar(10) primary key not null,
            work_times int not null default 0);
            """
        )

        print("Create users table")

        conn.close()

    def get_work_times(self, user_name): #db
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.execute(
            f"SELECT work_times FROM users WHERE name = '{user_name}'"
        )

        first_row = cursor.fetchone()
        print(f"{first_row=}")
        
        if first_row:
            return first_row[0]
        else:
            return None

    def insert_user(self, user_name): # db
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.execute(
            f"INSERT OR IGNORE INTO users (name, work_times) VALUES ('{user_name}', 0)"
        )
        conn.commit()
        conn.close()

    def increase_work_times(self, user_name):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.execute(
            f"UPDATE users SET work_times = work_times + 1 WHERE name = '{user_name}'"
        )
        conn.commit()
        conn.close()