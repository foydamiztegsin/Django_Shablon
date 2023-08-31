from environs import Env


env = Env()
env.read_env()

# settings.py
SECRET_KEY    = env.str("SECRET_KEY")
DEBUG         = env.str("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# PostgreSQL
DB_NAME       = env.str("DB_NAME")
DB_USER       = env.str("DB_USER")
DB_PASS       = env.str("DB_PASS")
DB_HOST       = env.str("DB_HOST")