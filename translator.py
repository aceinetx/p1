from language_database import LanguageDatabase

class Translator:
    def __init__(self, db: LanguageDatabase):
        self.db = db

    def translate(self, code: str) -> str:
        functions = self.db.get_functions()
        for function in functions:
            code = code.replace(function.name, function.translate_to)
        return code
