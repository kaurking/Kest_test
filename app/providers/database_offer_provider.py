import logging
import sqlite3

from app.database import connect, create_schema

logger = logging.getLogger(__name__)


class DatabaseOfferProvider:
    def __init__(self, database_url: str | None = None):
        self.database_url = database_url

    def get_offers_for_registration(self, registration_number: str) -> list[dict]:
        try:
            connection = connect(self.database_url) if self.database_url else connect()
            create_schema(connection)
            rows = connection.execute(
                """
                SELECT reg, insurer, product, premium, period, currency, status, error
                FROM offers
                WHERE upper(reg) = upper(?)
                ORDER BY id
                """,
                (registration_number,),
            ).fetchall()
        except sqlite3.Error as error:
            logger.exception(
                "database_query_failed operation=get_offers_for_registration"
            )
            raise RuntimeError("Database query failed") from error
        finally:
            if "connection" in locals():
                connection.close()

        offers = [dict(row) for row in rows]
        logger.info(
            "mtpl_offers_loaded registration=%s raw_count=%s",
            registration_number,
            len(offers),
        )
        return offers
