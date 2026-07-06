import re


class InvalidRegistrationNumber(ValueError):
    pass


def normalize_registration_number(value: str) -> str:
    if value is None:
        raise InvalidRegistrationNumber("Registration number is required")

    normalized = re.sub(r"[\s-]+", "", value).upper()
    if not normalized:
        raise InvalidRegistrationNumber("Registration number is required")

    return normalized
