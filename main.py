import sys
from language_database import *

def main() -> int:
    db = LanguageDatabase()
    db.add(Function("x", 2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
