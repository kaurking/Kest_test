from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.domain.registration import InvalidRegistrationNumber
from app.logging_config import configure_logging
from app.providers.database_offer_provider import DatabaseOfferProvider
from app.services.quote_service import (
    NoOffersFound,
    NoValidMtplOffersFound,
    QuoteService,
)

BASE_DIR = Path(__file__).resolve().parent.parent

configure_logging()

app = FastAPI(title="MTPL Quote API")
quote_service = QuoteService(DatabaseOfferProvider())
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "app" / "static" / "index.html")


@app.get("/api/mtpl/offers")
def get_mtpl_offers(
    registration_number: str = Query(..., min_length=1),
) -> dict:
    try:
        return quote_service.get_cheapest_mtpl_offer(registration_number)
    except InvalidRegistrationNumber as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except NoOffersFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    except NoValidMtplOffersFound as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
