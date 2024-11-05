from dotenv import load_dotenv
import os
import os

load_dotenv()

ENVIRONMENT = os.environ.get("ENVIRONMENT")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

TEST_DB_HOST = os.environ.get("TEST_DB_HOST")
TEST_DB_PORT = os.environ.get("TEST_DB_PORT")
TEST_DB_NAME = os.environ.get("TEST_DB_NAME")
TEST_DB_USER = os.environ.get("TEST_DB_USER")
TEST_DB_PASS = os.environ.get("TEST_DB_PASS")

ADMIN_LOGIN = os.environ.get("ADMIN_LOGIN")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")


SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")


def get_db_url():
    return (f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@"
            f"{DB_HOST}:{DB_PORT}/{DB_NAME}")


def test_get_db_url():
    return (f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASS}@"
            f"{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}")


def get_auth_data():
    return {"secret_key": SECRET_KEY, "algorithm": ALGORITHM}
