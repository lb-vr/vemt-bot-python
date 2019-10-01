import os


def loadTokenFromFile() -> str:
    with open(os.path.join(os.getcwd(), 'config/token.txt'), mode='r', encoding='utf-8') as f:
        return f.readline().strip()
