from app.domain.price import SUPPORTED_PERIODS, annual_premium, format_amount

MTPL_PRODUCT = "mtpl"
TOP_OFFERS_LIMIT = 3


def build_comparable_offer(raw_offer: dict) -> tuple[dict | None, str | None]:
    if raw_offer.get("product") != MTPL_PRODUCT:
        return None, "not_mtpl"

    if raw_offer.get("status") != "ok":
        return None, "offer_error"

    premium = raw_offer.get("premium")
    if not isinstance(premium, (int, float)):
        return None, "missing_premium"

    period = raw_offer.get("period")
    if period not in SUPPORTED_PERIODS:
        return None, "unsupported_period"

    currency = raw_offer.get("currency")
    if currency != "EUR":
        return None, "unsupported_currency"

    annual = annual_premium(premium, period)

    return {
        "insurer": raw_offer.get("insurer"),
        "product": raw_offer.get("product"),
        "premium": format_amount(premium),
        "period": period,
        "currency": currency,
        "annualPremium": format_amount(annual),
    }, None


def compare_mtpl_offers(raw_offers: list[dict]) -> dict:
    valid_offers = []
    ignored_offers = []

    for offer in raw_offers:
        comparable_offer, ignore_reason = build_comparable_offer(offer)
        if comparable_offer:
            valid_offers.append(comparable_offer)
        else:
            ignored_offers.append({
                "insurer": offer.get("insurer"),
                "reason": ignore_reason,
            })

    valid_offers.sort(key=lambda offer: (offer["annualPremium"], offer["insurer"] or ""))

    if not valid_offers:
        return {
            "cheapestOffer": None,
            "cheapestOffers": [],
            "topOffers": [],
            "offers": [],
            "comparedOffers": 0,
            "ignoredOffers": ignored_offers,
        }

    cheapest_price = valid_offers[0]["annualPremium"]
    cheapest_offers = [
        offer for offer in valid_offers if offer["annualPremium"] == cheapest_price
    ]

    return {
        "cheapestOffer": valid_offers[0],
        "cheapestOffers": cheapest_offers,
        "topOffers": valid_offers[:TOP_OFFERS_LIMIT],
        "offers": valid_offers,
        "comparedOffers": len(valid_offers),
        "ignoredOffers": ignored_offers,
    }
