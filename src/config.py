
DB_HOST = '127.0.0.1'
DB_PORT = "5434"
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'univ'

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
