import sys
from language_database import *
from function import Function

def main() -> int:
    db = LanguageDatabase()
    db.add(Function("Для ч в строка", 0, "for x in string:"))
    db.add(Function("Пиши_давай!", 0, "print"))
    db.add(Function("есть_чо_сказать?", 0, "input"))
    db.add(Function("Коли", 0, "if"))
    db.add(Function("Э,_стапе", 0, "break"))
    db.add(Function("Разбосище", 0, "range"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
