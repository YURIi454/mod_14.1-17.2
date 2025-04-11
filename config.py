import os

ROOT_DIR = os.path.dirname(__file__)
LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
DATA_DIR = os.path.join(ROOT_DIR, 'data')

PATH_JSON = os.path.join(DATA_DIR, 'products.json')
PATH_CSV = ''
PATH_XLSX = os.path.join(DATA_DIR)
PATH_LOGS = os.path.join(LOGS_DIR, 'logs.log')

for_test = ('pytest;isort main.py src tests;black main.py src tests;mypy '
              'main.py src tests;flake8 main.py src tests;pytest --cov=src --cov-report=html;')
