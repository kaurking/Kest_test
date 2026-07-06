import logging

from app.domain.offer_comparison import compare_mtpl_offers
from app.domain.registration import normalize_registration_number

logger = logging.getLogger(__name__)


class NoOffersFound(LookupError):
    pass


class NoValidMtplOffersFound(LookupError):
    pass


class QuoteService:
    def __init__(self, offer_provider):
        self.offer_provider = offer_provider

    def get_cheapest_mtpl_offer(self, registration_number: str) -> dict:
        normalized_registration = normalize_registration_number(registration_number)
        logger.info(
            "mtpl_offers_requested registration=%s",
            normalized_registration,
        )

        raw_offers = self.offer_provider.get_offers_for_registration(normalized_registration)

        if not raw_offers:
            logger.info(
                "mtpl_offers_not_found registration=%s",
                normalized_registration,
            )
            raise NoOffersFound("No offers found for registration number")

        comparison = compare_mtpl_offers(raw_offers)
        if comparison["cheapestOffer"] is None:
            logger.info(
                "mtpl_valid_offers_not_found registration=%s raw_count=%s ignored_count=%s",
                normalized_registration,
                len(raw_offers),
                len(comparison["ignoredOffers"]),
            )
            raise NoValidMtplOffersFound("No valid MTPL offers found")

        cheapest_offer = comparison["cheapestOffer"]
        logger.info(
            "mtpl_offers_compared registration=%s raw_count=%s valid_count=%s ignored_count=%s cheapest_insurer=%s cheapest_annual_premium=%s",
            normalized_registration,
            len(raw_offers),
            comparison["comparedOffers"],
            len(comparison["ignoredOffers"]),
            cheapest_offer["insurer"],
            cheapest_offer["annualPremium"],
        )

        return {
            "registrationNumber": normalized_registration,
            **comparison,
        }
