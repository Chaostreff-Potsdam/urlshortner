import os
import sys
sys.path.append(os.getcwd())
from wsgi import db

if __name__ == '__main__':
    db.create_all()
