import sys
from language_database import *
from function import Function
from translator import Translator

def main() -> int:
    db = LanguageDatabase()
    db.add(Function("Для ч в", "for ч in"))
    db.add(Function("Пиши_давай!", "print"))
    db.add(Function("есть_чо_сказать?", "input"))
    db.add(Function("число", "int"))
    db.add(Function("Коли", "if"))
    db.add(Function("Э,_стапе", "break"))
    db.add(Function("Разбросище", "range"))

    translator = Translator(db)
    code = translator.translate('''
х = число(есть_чо_сказать?())
Для ч в Разбросище(0, х):
    Пиши_давай!(ч)
    Коли ч == х // 2:
        Пиши_давай!("")
        Э,_стапе
    ''')
    print(code)
    exec(code)
    return 0

if __name__ == "__main__":
    sys.exit(main())
