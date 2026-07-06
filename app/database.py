import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATABASE_PATH = BASE_DIR / "data" / "app.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DATABASE_PATH}")


class DatabaseNotConfigured(RuntimeError):
    pass


def get_database_path(database_url: str = DATABASE_URL) -> Path:
    prefix = "sqlite:///"
    if not database_url.startswith(prefix):
        raise DatabaseNotConfigured("Only sqlite:/// DATABASE_URL values are supported")

    return Path(database_url.removeprefix(prefix))


def connect(database_url: str = DATABASE_URL) -> sqlite3.Connection:
    database_path = get_database_path(database_url)
    database_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def create_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg TEXT NOT NULL,
            insurer TEXT NOT NULL,
            product TEXT NOT NULL,
            premium REAL,
            period TEXT NOT NULL,
            currency TEXT NOT NULL,
            status TEXT NOT NULL,
            error TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.execute(
        "CREATE INDEX IF NOT EXISTS idx_offers_reg ON offers (reg)"
    )
    connection.commit()
