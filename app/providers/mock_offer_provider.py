import json
from pathlib import Path


class MockOfferProvider:
    def __init__(self, offers_file: Path):
        self.offers_file = offers_file

    def get_offers_for_registration(self, registration_number: str) -> list[dict]:
        with self.offers_file.open(encoding="utf-8") as file:
            offers = json.load(file)

        return [
            offer
            for offer in offers
            if offer.get("reg", "").upper() == registration_number
        ]
