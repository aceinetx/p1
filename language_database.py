import sqlite3
from function import Function

class LanguageDatabase:
    def __init__(self):
        self.db = sqlite3.connect("language.db")
        self.cur = self.db.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS language (
            name TEXT,
            translate_to TEXT
        )
        """)

        self.db.commit()

    def __del__(self):
        self.db.close()

    def add(self, function: Function) -> None:
        self.cur.execute("""
        INSERT INTO language (name, translate_to) VALUES (?, ?)
        """, (function.name, function.translate_to))
        self.db.commit()

    def get_function(self, name: str) -> Function:
        self.cur.execute("""
        SELECT name, translate_to FROM language WHERE function = ?
        """, (name))
        row = self.cur.fetchall()
        return Function(row[0][0], row[0][1])
    
    def get_functions(self) -> [Function]:
        self.cur.execute("""
        SELECT name, translate_to FROM language
        """)
        rows = self.cur.fetchall()
        functions = []
        for row in rows:
            functions.append(Function(row[0], row[1]))
        return functions
