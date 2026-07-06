SUPPORTED_PERIODS = {"month", "year"}


def annual_premium(premium: float, period: str) -> float:
    if period == "year":
        return premium
    if period == "month":
        return premium * 12
    raise ValueError(f"Unsupported period: {period}")


def format_amount(value: float) -> int | float:
    return int(value) if value == int(value) else value
