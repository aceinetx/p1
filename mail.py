from translator import Translator

class Mail:
    def __init__(self, id_, text):
        self.id_ = id_
        self.text = text

    def translate(self, translator: Translator) -> str:
        return translator.translate(self.text)
