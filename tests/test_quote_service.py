import unittest

from app.domain.registration import InvalidRegistrationNumber, normalize_registration_number
from app.services.quote_service import NoOffersFound, QuoteService


class InMemoryOfferProvider:
    def __init__(self, offers):
        self.offers = offers

    def get_offers_for_registration(self, registration_number):
        return [
            offer
            for offer in self.offers
            if offer.get("reg", "").upper() == registration_number
        ]


class QuoteServiceTest(unittest.TestCase):
    def test_finds_cheapest_mtpl_offer_by_annual_price(self):
        service = QuoteService(InMemoryOfferProvider([
            {
                "reg": "123ABC",
                "insurer": "If",
                "product": "mtpl",
                "premium": 245,
                "period": "year",
                "currency": "EUR",
                "status": "ok",
            },
            {
                "reg": "123ABC",
                "insurer": "Salva",
                "product": "mtpl",
                "premium": 18,
                "period": "month",
                "currency": "EUR",
                "status": "ok",
            },
            {
                "reg": "123ABC",
                "insurer": "Ergo",
                "product": "mtpl",
                "premium": 199,
                "period": "year",
                "currency": "EUR",
                "status": "ok",
            },
        ]))

        result = service.get_cheapest_mtpl_offer("123 abc")

        self.assertEqual(result["registrationNumber"], "123ABC")
        self.assertEqual(result["cheapestOffer"]["insurer"], "Ergo")
        self.assertEqual(result["cheapestOffer"]["annualPremium"], 199)
        self.assertEqual(result["comparedOffers"], 3)

    def test_ignores_non_mtpl_and_error_offers(self):
        service = QuoteService(InMemoryOfferProvider([
            {
                "reg": "123ABC",
                "insurer": "PZU",
                "product": "casco",
                "premium": 175,
                "period": "year",
                "currency": "EUR",
                "status": "ok",
            },
            {
                "reg": "123ABC",
                "insurer": "Gjensidige",
                "product": "mtpl",
                "premium": None,
                "period": "year",
                "currency": "EUR",
                "status": "error",
            },
            {
                "reg": "123ABC",
                "insurer": "LHV",
                "product": "mtpl",
                "premium": 199,
                "period": "year",
                "currency": "EUR",
                "status": "ok",
            },
        ]))

        result = service.get_cheapest_mtpl_offer("123ABC")

        self.assertEqual(result["cheapestOffer"]["insurer"], "LHV")
        self.assertEqual(result["comparedOffers"], 1)
        self.assertEqual(
            [ignored["reason"] for ignored in result["ignoredOffers"]],
            ["not_mtpl", "offer_error"],
        )

    def test_raises_when_no_offers_exist_for_registration(self):
        service = QuoteService(InMemoryOfferProvider([]))

        with self.assertRaises(NoOffersFound):
            service.get_cheapest_mtpl_offer("999ZZZ")

    def test_normalizes_registration_number(self):
        self.assertEqual(normalize_registration_number(" 123-abc "), "123ABC")

    def test_rejects_blank_registration_number(self):
        with self.assertRaises(InvalidRegistrationNumber):
            normalize_registration_number("   ")


if __name__ == "__main__":
    unittest.main()
