import sqlite3
from function import Function

class LanguageDatabase:
    def __init__(self):
        self.db = sqlite3.connect("language.db")
        self.cur = self.db.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS language (
            function TEXT,
            arguments INTEGER
        )
        """)

        self.db.commit()

    def __del__(self):
        self.db.close()

    def add(self, function: Function) -> None:
        self.cur.execute("""
        INSERT INTO language (function, arguments) VALUES (?, ?)
        """, (function.name, function.argument_count))
        self.db.commit()

    def get_function(self, name: str) -> Function:
        self.cur.execute("""
        SELECT function, arguments FROM language WHERE function = ?
        """, (name))
        row = self.cur.fetchall()
        return Function(row[0][0], row[0][1])

