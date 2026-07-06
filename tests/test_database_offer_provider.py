import sqlite3
import tempfile
import unittest
from pathlib import Path

from app.database import create_schema
from app.providers.database_offer_provider import DatabaseOfferProvider


class DatabaseOfferProviderTest(unittest.TestCase):
    def test_reads_offers_for_registration_from_sqlite(self):
        with tempfile.TemporaryDirectory() as directory:
            database_path = Path(directory) / "test.db"
            database_url = f"sqlite:///{database_path}"

            connection = sqlite3.connect(database_path)
            create_schema(connection)
            connection.executemany(
                """
                INSERT INTO offers
                    (reg, insurer, product, premium, period, currency, status, error)
                VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    ("123ABC", "If", "mtpl", 245, "year", "EUR", "ok", None),
                    ("123ABC", "Ergo", "mtpl", 199, "year", "EUR", "ok", None),
                    ("456DEF", "Seesam", "mtpl", 299, "year", "EUR", "ok", None),
                ],
            )
            connection.commit()
            connection.close()

            provider = DatabaseOfferProvider(database_url)

            offers = provider.get_offers_for_registration("123ABC")

            self.assertEqual(len(offers), 2)
            self.assertEqual([offer["insurer"] for offer in offers], ["If", "Ergo"])


if __name__ == "__main__":
    unittest.main()
