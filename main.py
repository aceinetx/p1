import sys
from language_database import *
from function import Function
from translator import Translator

def main() -> int:
    db = LanguageDatabase()
    db.add(Function("Для ч в", 0, "for ч in"))
    db.add(Function("Пиши_давай!", 0, "print"))
    db.add(Function("есть_чо_сказать?", 0, "input"))
    db.add(Function("число", 0, "int"))
    db.add(Function("Коли", 0, "if"))
    db.add(Function("Э,_стапе", 0, "break"))
    db.add(Function("Разбросище", 0, "range"))

    translator = Translator(db)
    code = translator.translate('''
х = число(есть_чо_сказать?())
Для ч в Разбросище(0, х):
    Пиши_давай!(ч)
    Коли ч == х // 2:
        Пиши_давай!("А все!")
        Э,_стапе
    ''')
    print(code)
    exec(code)
    return 0

if __name__ == "__main__":
    sys.exit(main())
