import sqlite3, uuid
from function import Function

class MailDatabase:
    def __init__(self):
        self.db = sqlite3.connect("language.db")
        self.cur = self.db.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS mails (
            uuid TEXT
        )
        """)

        self.db.commit()

    def __del__(self):
        self.db.close()

    def add(self, text: str) -> None:
        id_ = uuid.uuid4()
        with open(f"mails/{id_}", "w") as f:
            f.write(text)

        print(str(id_))
        self.cur.execute("""
        INSERT INTO mails (`uuid`) VALUES (?)
        """, (str(id_)))
        self.db.commit()
